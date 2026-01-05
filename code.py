"""
Minimal ESP32 MicroPython web control interface for a high-speed RC car.
- Starts an access point (change SSID/PASSWORD below).
- Serves a small HTML control page at http://192.168.4.1/ (default AP IP).
- Supports throttle/steering (PWM) plus a headlight toggle.
This is a sample; adapt pins, PWM ranges, and safety limits for your hardware.
"""

import network
import socket
import time
import json
from machine import Pin, PWM

# ---- User configuration ----
SSID = "Zephyr-RC"
PASSWORD = "rc-car-1234"  # Change for production

THROTTLE_PIN = 14  # PWM-capable pin to motor controller
STEERING_PIN = 27   # PWM-capable pin to steering servo
HEADLIGHT_PIN = 26  # Simple digital output

PWM_FREQ = 50  # Typical servo frequency; change to match ESC if needed
THROTTLE_MIN_US = 1000  # Microseconds
THROTTLE_MAX_US = 2000
STEERING_MIN_US = 1000
STEERING_MAX_US = 2000

# ---- Hardware setup ----
throttle_pwm = PWM(Pin(THROTTLE_PIN), freq=PWM_FREQ)
steering_pwm = PWM(Pin(STEERING_PIN), freq=PWM_FREQ)
headlight = Pin(HEADLIGHT_PIN, Pin.OUT)

# MicroPython PWM duty for 16-bit resolution
PWM_RES = 65535

# Clamp helpers

def clamp(val: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, val))


def us_to_duty(us: int) -> int:
    # Convert microseconds to duty for given frequency.
    period_us = 1_000_000 // PWM_FREQ
    duty = int((clamp(us, 0, period_us) / period_us) * PWM_RES)
    return clamp(duty, 0, PWM_RES)


# ---- Networking ----

def start_ap():
    ap = network.WLAN(network.AP_IF)
    ap.active(True)
    ap.config(essid=SSID, password=PASSWORD)
    while not ap.active():
        time.sleep(0.1)
    ip = ap.ifconfig()[0]
    print("AP started on:", ip)
    return ip


# ---- Control state ----
state = {
    "throttle": 0,  # 0-100 percent
    "steering": 0,  # -100 (left) to 100 (right)
    "lights": False,
}


def apply_outputs():
    # Map throttle percent to PWM range.
    throttle_span = THROTTLE_MAX_US - THROTTLE_MIN_US
    throttle_us = THROTTLE_MIN_US + int((state["throttle"] / 100) * throttle_span)
    throttle_pwm.duty_u16(us_to_duty(throttle_us))

    # Map steering percent to PWM range around center.
    steer_span = STEERING_MAX_US - STEERING_MIN_US
    steer_us = STEERING_MIN_US + int(((state["steering"] + 100) / 200) * steer_span)
    steering_pwm.duty_u16(us_to_duty(steer_us))

    headlight.value(1 if state["lights"] else 0)


# ---- HTTP helpers ----
INDEX_HTML = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Zephyr RC Control</title>
  <style>
    body { font-family: Arial, sans-serif; background:#0d1117; color:#e6edf3; margin:0; padding:16px; }
    h1 { margin-top:0; }
    .card { background:#161b22; border:1px solid #30363d; border-radius:10px; padding:16px; max-width:480px; }
    label { display:block; margin-top:12px; }
    input[type=\"range\"] { width:100%; }
    .row { display:flex; gap:12px; align-items:center; }
    button { padding:10px 14px; border:none; border-radius:8px; background:#238636; color:white; font-weight:700; cursor:pointer; }
    button.stop { background:#d1083f; }
    .status { margin-top:12px; font-size:14px; color:#8b949e; }
  </style>
</head>
<body>
  <div class=\"card\">
    <h1>Zephyr RC</h1>
    <label>Throttle: <span id=\"throttleVal\">0</span>%</label>
    <input id=\"throttle\" type=\"range\" min=\"0\" max=\"100\" step=\"1\" value=\"0\" />

    <label>Steering: <span id=\"steerVal\">0</span>%</label>
    <input id=\"steer\" type=\"range\" min=\"-100\" max=\"100\" step=\"1\" value=\"0\" />

    <div class=\"row\" style=\"margin-top:12px;\">
      <label><input id=\"lights\" type=\"checkbox\" /> Headlights</label>
    </div>

    <div class=\"row\" style=\"margin-top:16px;\">
      <button id=\"apply\">Send</button>
      <button class=\"stop\" id=\"stop\">Stop</button>
    </div>

    <div class=\"status\" id=\"status\">Idle</div>
  </div>

<script>
const $ = (id) => document.getElementById(id);
const statusEl = $("status");

function updateLabels() {
  $("throttleVal").textContent = $("throttle").value;
  $("steerVal").textContent = $("steer").value;
}

function sendState(throttle, steering, lights) {
  statusEl.textContent = "Sending...";
  fetch(`/set?throttle=${throttle}&steering=${steering}&lights=${lights ? 1 : 0}`)
    .then(() => statusEl.textContent = "OK")
    .catch(() => statusEl.textContent = "Failed");
}

$("apply").onclick = () => {
  updateLabels();
  sendState($("throttle").value, $("steer").value, $("lights").checked);
};

$("stop").onclick = () => {
  $("throttle").value = 0;
  $("steer").value = 0;
  $("lights").checked = false;
  updateLabels();
  sendState(0, 0, false);
};

$("throttle").oninput = updateLabels;
$("steer").oninput = updateLabels;
</script>
</body>
</html>
"""


def build_response(body: str, content_type: str = "text/html") -> bytes:
    headers = [
        "HTTP/1.1 200 OK",
        f"Content-Type: {content_type}; charset=utf-8",
        "Cache-Control: no-store",
        "Connection: close",
        "",
        "",
    ]
    return "\r\n".join(headers).encode() + body.encode()


def parse_query(path: str) -> dict:
    if "?" not in path:
        return {}
    _, query = path.split("?", 1)
    params = {}
    for pair in query.split("&"):
        if not pair:
            continue
        if "=" in pair:
            k, v = pair.split("=", 1)
        else:
            k, v = pair, ""
        params[k] = v
    return params


def handle_request(conn):
    req = conn.recv(1024)
    if not req:
        return
    try:
        line = req.decode().split("\r\n")[0]
        method, path, _ = line.split(" ")
    except Exception:
        conn.send(build_response("Bad Request", "text/plain"))
        return

    if path.startswith("/set"):
        params = parse_query(path)
        throttle = clamp(int(params.get("throttle", state["throttle"])), 0, 100)
        steering = clamp(int(params.get("steering", state["steering"])), -100, 100)
        lights = params.get("lights", "0") in ("1", "true", "on")

        state.update({"throttle": throttle, "steering": steering, "lights": lights})
        apply_outputs()
        payload = json.dumps(state)
        conn.send(build_response(payload, "application/json"))
        return

    if path.startswith("/state"):
        payload = json.dumps(state)
        conn.send(build_response(payload, "application/json"))
        return

    # Default: serve control page
    conn.send(build_response(INDEX_HTML))


def serve(ip: str):
    addr = (ip, 80)
    s = socket.socket()
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(addr)
    s.listen(2)
    print("Listening on", addr)
    while True:
        conn, _ = s.accept()
        handle_request(conn)
        conn.close()


def main():
    ip = start_ap()
    apply_outputs()  # Initialize outputs to safe defaults
    serve(ip)


if __name__ == "__main__":
    main()
