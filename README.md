# Zephyr
---

## What it is
Zephyr is a high-performance RC Hypercar that I am building. It has 2 main focuses in regard to performance, both **max top speed** and also **good cornering/f1 style racing**. 

### Performance Specs
* **Top Speed:** The max speed is achieved by its 4300kv single motor which drives the rear wheel shaft, which is built around a pretty lean gear ratio which in turn enables it to hit max speeds of 40-50MPH straight line.
* **Precision Steering:** On the cornering aspect of things, I am using a 20KG Digital servo to handle steering, utilizing steel cables to turn 2 front wheels, this enables me to have strong steering as well as allows me to use variable Ackerman Steering configurations by changing the tighnesses of each of the 4 cables.
* **Active Aerodynamics:** Also, this hypercar also has Active Aero enabled by dual SG90 servos that drive a inverted-airfoil rear wing! This in turn allows me to generate a lot of downforce on demand, which is pivotal in circuit racing as well as allows me to brake a lot faster while keeping my custom gear reduction system intact! 
* **FPV System:** Zephyr also comes with on-board FPV with its custom designed controller module that enables live feedback and video streaming using an esp32-s3 and an OV2640 sensor!

---

## Why I made it
I have always wanted to build my own rc-car, and have attempted to in the past but never got to actually building it. Hence, when **#blueprint by hackclub** came along, one of the first projects I wanted to make was a rc hypercar. 

Beyond this, I really wanted to use brushless motors and ESCs because I've always only had the oppurtunity to work with low power DC motors. Also, honestly, this was a giant step in my journey of cad, having only really built low-spec projects in cad before like cubes! So building and designing this, the steering system, the power and transmisson, as well as the chassis, was a massive personal accomplishment. In fact, I had never used a lot of the tools like chamfer, draft, and loft in fusion 360 let alone design gears or tires before so this gave me a really big learning curve.

---

## How I made it (Making Process)

1.  I drafted the overall electical diagram, decided on parts as well as the overall characteristics
2.  Finalized parts and started on Schematic
3.  Finished the Schematic, Finished the PCB layout as well
4.  Finished the rest of the PCB
5.  Started on the cad, first did the front and rear wing
6.  Then did the wheels (pneumatic tire design, really proud of that)
7.  Then did the transmission system with the gears and rear setup
8.  Then did the steering (went through like 4 iterations before finalizing the cable based setup)
9.  Then did the base chassis (ie the areas for the esc, battery, pcb, wheel cutouts, rear axel holders, and a lot of integrating different components)
10. Then spent a lot of time on the outer "Shell", which took so long because I wanted to get the Lemans hypercar esque look, tryed to use canvases and sketch around that but that did not end up working
11. Somehow pulled through and finished that, then did the GH repo, finished BOM and did all else required for submission!

---

##  Future Roadmap
What is are the next steps for zephyr (how can I improve it)?
- [ ] **Add a rear differential** (hella complex) so that better cornering
- [ ] **Make the gear system a lot more robust** so it can handle a lot bigger of a motor
- [ ] **Rely less on bushels** for the steering system
- [ ] **Add a larger, more powerful battery** for more performance and longevity
- [ ] **Make the front wing active** as well
- [ ] **Add headlights**

---

## Hardware & Electronics

### PCB Layouts
<img width="951" height="644" alt="Screenshot 2025-12-29 201159" src="https://github.com/user-attachments/assets/912e2da1-bb84-4a03-bf9c-3fcf89a00d85" />
<img width="1258" height="803" alt="Screenshot 2025-12-29 201152" src="https://github.com/user-attachments/assets/f2ef01df-1502-42f8-93f9-52b8a63bbeb6" />
<img width="584" height="534" alt="Screenshot 2025-12-29 195615" src="https://github.com/user-attachments/assets/b3ecd6bd-17fd-4adf-bb35-f1481e427990" />
<img width="606" height="545" alt="Screenshot 2025-12-29 195607" src="https://github.com/user-attachments/assets/20735c59-4377-450b-a8e1-7c53cb487b63" />
<img width="955" height="785" alt="Screenshot 2025-12-29 171313" src="https://github.com/user-attachments/assets/6da403b2-0619-4ac6-9a17-5d6c291c61d2" />
<img width="1117" height="833" alt="Screenshot 2025-12-29 155954" src="https://github.com/user-attachments/assets/0a5f130e-3b3b-49f5-a2e3-2e5d3fff0e3f" />
<img width="1012" height="790" alt="Screenshot 2025-12-29 155646" src="https://github.com/user-attachments/assets/7174f15b-76b4-4a5a-8344-170f998f0c03" />

### Wiring Diagram & Bottom Chassis
<img width="1054" height="501" alt="Untitled" src="https://github.com/user-attachments/assets/7567dc4f-1b2d-4611-8909-86d069f521b6" />
<img width="1391" height="505" alt="Screenshot 2026-01-07 210737" src="https://github.com/user-attachments/assets/e49a0b35-29b2-4221-b373-24204a354468" />



PCB Gerber:

[Gerber_PCB1_2026-01-17.zip](https://github.com/user-attachments/files/24690630/Gerber_PCB1_2026-01-17.zip)
