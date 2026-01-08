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

##CAD Montage (Process Gallery)
<img width="992" height="419" alt="Screenshot 2020-12-30 123725 - Copy - Copy" src="https://github.com/user-attachments/assets/62475ca1-f334-47be-880a-3617502a63b5" />
<img width="1239" height="394" alt="Screenshot 2025-12-30 145535 - Copy - Copy - Copy" src="https://github.com/user-attachments/assets/7f21ca07-9b2f-45dc-b344-41db0f5735ba" />
<img width="1239" height="394" alt="Screenshot 2025-12-30 145535 - Copy (2) - Copy" src="https://github.com/user-attachments/assets/efc99137-a25f-4a66-a092-c7e18e87b3cf" />
<img width="473" height="385" alt="Screenshot 2025-12-30 145541 - Copy - Copy - Copy" src="https://github.com/user-attachments/assets/914ab86b-d9ec-467b-a072-f7c995a9a775" />
<img width="473" height="385" alt="Screenshot 2025-12-30 145541 - Copy (2) - Copy" src="https://github.com/user-attachments/assets/fffa7042-9fc5-4453-859c-443608e4c614" />
<img width="309" height="208" alt="Screenshot 2025-12-30 145804 - Copy - Copy" src="https://github.com/user-attachments/assets/682c60c8-9bd3-4258-ad3e-8239173bdfdc" />
<img width="1134" height="513" alt="Screenshot 2025-12-30 150232 - Copy - Copy - Copy" src="https://github.com/user-attachments/assets/3bee46a3-33f0-48f8-be15-b48b4db76855" />
<img width="1134" height="513" alt="Screenshot 2025-12-30 150232 - Copy (2) - Copy" src="https://github.com/user-attachments/assets/6cf5d238-469e-4f92-b230-61285744c1ca" />
<img width="958" height="460" alt="Screenshot 2025-12-30 155610 - Copy - Copy" src="https://github.com/user-attachments/assets/3554f5ed-2128-4566-88be-9e9bb293267e" />
<img width="1289" height="620" alt="Screenshot 2025-12-30 155635 - Copy - Copy" src="https://github.com/user-attachments/assets/cc8b7b58-16ba-4dd3-8dc8-ccd1abbf41c9" />
<img width="1405" height="715" alt="Screenshot 2025-12-30 194448 - Copy - Copy" src="https://github.com/user-attachments/assets/c10fd18b-ddc3-433d-9e17-9e2ec0664135" />
<img width="1146" height="408" alt="Screenshot 2025-12-30 194456 - Copy - Copy" src="https://github.com/user-attachments/assets/1bdac6b1-0e91-4091-ab2e-630c88ced160" />
<img width="630" height="351" alt="Screenshot 2025-12-30 194509 - Copy - Copy" src="https://github.com/user-attachments/assets/762a7b93-8a8a-4fbf-8b85-254496208e56" />
<img width="676" height="568" alt="Screenshot 2025-12-30 195111 - Copy - Copy" src="https://github.com/user-attachments/assets/f649f13d-8f01-4105-af39-55b9c5347a31" />
<img width="954" height="718" alt="Screenshot 2025-12-30 225437 - Copy - Copy" src="https://github.com/user-attachments/assets/d1787762-d76b-437c-8e8f-88b5c4254bbe" />
<img width="1151" height="745" alt="Screenshot 2025-12-31 000808 - Copy - Copy" src="https://github.com/user-attachments/assets/920c0b34-096d-4b57-bbca-fa6cd6e7c509" />
<img width="1067" height="636" alt="Screenshot 2025-12-31 001010 - Copy - Copy" src="https://github.com/user-attachments/assets/52e0ae54-ff28-438d-b21a-54ca2a8d1f0f" />
<img width="863" height="848" alt="Screenshot 2025-12-31 125204 - Copy - Copy" src="https://github.com/user-attachments/assets/0e5f96c7-2434-4d69-b4f3-21339f694786" />
<img width="691" height="701" alt="Screenshot 2025-12-31 150527 - Copy - Copy" src="https://github.com/user-attachments/assets/0df4113c-279f-4477-a0f9-8c9054e97671" />
<img width="811" height="741" alt="Screenshot 2025-12-31 153500 - Copy - Copy" src="https://github.com/user-attachments/assets/dd96c471-49fb-4a0d-b60a-b9a9cedf2d76" />
<img width="758" height="646" alt="Screenshot 2025-12-31 153512 - Copy - Copy" src="https://github.com/user-attachments/assets/6d142948-9094-4e9e-856c-7fa1879225d4" />
<img width="900" height="749" alt="Screenshot 2025-12-31 153521 - Copy - Copy" src="https://github.com/user-attachments/assets/d2f973b8-66d6-4efd-a917-47e51b630cf6" />
<img width="901" height="520" alt="Screenshot 2025-12-31 154503 - Copy - Copy" src="https://github.com/user-attachments/assets/f8120381-7fad-44a5-b9fe-693b503feea3" />
<img width="584" height="353" alt="Screenshot 2025-12-31 155602 - Copy - Copy" src="https://github.com/user-attachments/assets/9e4ffa3b-d62c-48b3-bbb7-614607956001" />
<img width="1098" height="597" alt="Screenshot 2025-12-31 160358 - Copy - Copy" src="https://github.com/user-attachments/assets/9013d1da-dc4f-4f2a-99f6-cdd90e14bfe3" />
<img width="401" height="632" alt="Screenshot 2025-12-31 160915 - Copy - Copy" src="https://github.com/user-attachments/assets/5ae65b9c-87f8-47c4-b58f-2f93b896590f" />
<img width="950" height="578" alt="Screenshot 2025-12-31 161100 - Copy - Copy" src="https://github.com/user-attachments/assets/32339c15-a3ee-4802-b5f4-669c75b7e761" />
<img width="680" height="1151" alt="Screenshot 2026-01-01 173558 - Copy - Copy" src="https://github.com/user-attachments/assets/4a06cccc-400a-418f-a534-1007637a8cf5" />
<img width="942" height="729" alt="Screenshot 2026-01-02 231249 - Copy - Copy" src="https://github.com/user-attachments/assets/123ccf12-1f4e-43ad-8e51-f01c8df540df" />
<img width="858" height="649" alt="Screenshot 2026-01-02 232201 - Copy - Copy" src="https://github.com/user-attachments/assets/cb517553-3bb2-4e74-a682-fae71f8d388f" />
<img width="760" height="406" alt="Screenshot 2026-01-02 232208 - Copy - Copy" src="https://github.com/user-attachments/assets/2f2804ba-934e-4074-8f28-f57d43c3b840" />
<img width="662" height="730" alt="Screenshot 2026-01-03 003006 - Copy - Copy" src="https://github.com/user-attachments/assets/28894d5b-39a5-41da-9d9f-53ffcd6fba59" />
<img width="1012" height="715" alt="Screenshot 2026-01-03 005715 - Copy - Copy" src="https://github.com/user-attachments/assets/6e21d75b-1786-43b1-a5ae-43d4499c5fc0" />
<img width="1285" height="619" alt="Screenshot 2026-01-03 122116 - Copy - Copy" src="https://github.com/user-attachments/assets/1b326fe0-6ead-44a6-b18b-ff8466adc153" />
<img width="1012" height="653" alt="Screenshot 2026-01-03 122131 - Copy - Copy" src="https://github.com/user-attachments/assets/63f3e38f-2c6e-4a1d-9b1e-33b86f5cd103" />
<img width="1112" height="661" alt="Screenshot 2026-01-03 140148 - Copy - Copy" src="https://github.com/user-attachments/assets/194bbc21-d20e-4f63-8efa-19a163e18df6" />
<img width="903" height="665" alt="Screenshot 2026-01-03 142213 - Copy - Copy" src="https://github.com/user-attachments/assets/8bc72f83-ce07-4a6c-ae41-ca904908aa1a" />
<img width="921" height="754" alt="Screenshot 2026-01-03 142822 - Copy - Copy" src="https://github.com/user-attachments/assets/f830766e-0628-4be0-b5f1-da5fbcf21ce7" />
<img width="1018" height="560" alt="Screenshot 2026-01-03 145910 - Copy - Copy" src="https://github.com/user-attachments/assets/2f22a252-bb6d-4771-b047-eb764d2733b2" />
<img width="820" height="674" alt="Screenshot 2026-01-03 150114 - Copy - Copy" src="https://github.com/user-attachments/assets/5e87293b-3e9c-4a2e-9ffc-1834c5b9efab" />
<img width="434" height="437" alt="Screenshot 2026-01-03 150537 - Copy - Copy" src="https://github.com/user-attachments/assets/433b83fb-037a-40a7-8fe4-7461d02684d3" />
<img width="908" height="826" alt="Screenshot 2026-01-03 151552 - Copy - Copy" src="https://github.com/user-attachments/assets/4b2c7da5-fa89-4a07-bdca-ea418dff3734" />
<img width="945" height="541" alt="Screenshot 2026-01-03 155020 - Copy - Copy" src="https://github.com/user-attachments/assets/ef210cd6-8865-467c-b1e9-e9def2cc8c38" />
<img width="832" height="431" alt="Screenshot 2026-01-03 160020 - Copy - Copy" src="https://github.com/user-attachments/assets/edfec6c8-68e4-4e2a-bc1a-301db7d146bb" />
<img width="1040" height="523" alt="Screenshot 2026-01-03 160027 - Copy - Copy" src="https://github.com/user-attachments/assets/9435b875-84ad-482c-9566-51dcf2f7b83c" />
<img width="1047" height="713" alt="Screenshot 2026-01-03 162508 - Copy - Copy" src="https://github.com/user-attachments/assets/cb379c11-3d1d-4c29-b940-da551ead124c" />
<img width="1041" height="738" alt="Screenshot 2026-01-03 181558 - Copy - Copy" src="https://github.com/user-attachments/assets/f0e3aed1-bb18-4617-b26e-db262da98a0b" />
<img width="1041" height="738" alt="Screenshot 2026-01-03 181558 - Copy (2)" src="https://github.com/user-attachments/assets/4c318ee1-0e27-4bfd-bf2e-f02ca1b17a48" />
<img width="1175" height="511" alt="Screenshot 2026-01-03 183243 - Copy" src="https://github.com/user-attachments/assets/eceeed48-4ea6-42e5-8fd0-b77bcc588915" />
<img width="403" height="359" alt="Screenshot 2026-01-04 112715 - Copy" src="https://github.com/user-attachments/assets/ba29b592-53e3-4d77-add5-95065c8f2c5a" />
<img width="1213" height="744" alt="Screenshot 2026-01-04 130246 - Copy" src="https://github.com/user-attachments/assets/26b19e9d-abee-4484-8f97-7ba984f011e3" />
<img width="525" height="490" alt="Screenshot 2026-01-04 133803 - Copy" src="https://github.com/user-attachments/assets/8fa78666-a157-4b1a-b626-4918b490c5a3" />
<img width="653" height="607" alt="Screenshot 2026-01-04 134336 - Copy" src="https://github.com/user-attachments/assets/ac054d76-26e7-4a5c-b291-3021a38eafd5" />
<img width="797" height="672" alt="Screenshot 2026-01-04 142225 - Copy" src="https://github.com/user-attachments/assets/58060126-28dc-4602-8147-9184fc0fc0e1" />
<img width="1161" height="736" alt="Screenshot 2026-01-04 150430 - Copy" src="https://github.com/user-attachments/assets/5c3807bf-be4f-4f18-afb0-54e5ee8f3674" />
<img width="686" height="824" alt="Screenshot 2026-01-04 151213 - Copy" src="https://github.com/user-attachments/assets/48f75707-c79c-4315-8580-322347f1eb99" />
<img width="967" height="835" alt="Screenshot 2026-01-04 152418 - Copy" src="https://github.com/user-attachments/assets/b79fca7e-1eab-4922-bcb9-1d3309535f59" />
<img width="594" height="483" alt="Screenshot 2026-01-04 152825 - Copy" src="https://github.com/user-attachments/assets/8331a0c7-27a7-4390-bbe8-ca2d79a91b9f" />
<img width="775" height="424" alt="Screenshot 2026-01-04 153114 - Copy" src="https://github.com/user-attachments/assets/9f8a124e-6b55-41cd-92b6-cfe97c894806" />
<img width="1077" height="673" alt="Screenshot 2026-01-04 153133 - Copy" src="https://github.com/user-attachments/assets/9c9910dc-11ea-49ca-8e66-0b71e04466c0" />
<img width="1077" height="673" alt="Screenshot 2026-01-04 153133" src="https://github.com/user-attachments/assets/99270e67-0e97-4264-ba4f-3e06f0406a44" />
<img width="637" height="876" alt="Screenshot 2026-01-04 153445 - Copy" src="https://github.com/user-attachments/assets/d0937f26-53ec-49b9-8138-8a87813285c2" />
<img width="637" height="876" alt="Screenshot 2026-01-04 153445" src="https://github.com/user-attachments/assets/f25fccde-b348-4d75-ab27-4ee6794832d8" />
<img width="1050" height="727" alt="Screenshot 2026-01-04 153944" src="https://github.com/user-attachments/assets/06702a40-da63-4554-bae8-2da21c2c14e5" />
<img width="827" height="567" alt="Screenshot 2026-01-04 154252" src="https://github.com/user-attachments/assets/a251a177-e52d-4f27-9668-35765358ad24" />
<img width="774" height="565" alt="Screenshot 2026-01-04 154317" src="https://github.com/user-attachments/assets/4bbbcc52-3d09-48d0-b2fc-21118424eb86" />
<img width="634" height="836" alt="Screenshot 2026-01-04 155737" src="https://github.com/user-attachments/assets/c724af60-d391-45bd-aab8-7422b960c482" />
<img width="686" height="705" alt="Screenshot 2026-01-04 155941" src="https://github.com/user-attachments/assets/59282a87-dea9-48ca-b709-81b87a1ffdbd" />
<img width="968" height="654" alt="Screenshot 2026-01-04 160414" src="https://github.com/user-attachments/assets/7501f8b3-8a9d-44d5-b836-d4488c030f7a" />
<img width="954" height="559" alt="Screenshot 2026-01-04 160422" src="https://github.com/user-attachments/assets/c72b9694-faa5-4b05-b0d6-c72b9694-faa5-4b05-b0d6-c72b9694-faa5-4b05-b0d6-c72b9694-faa5-4b05-b0d6-c72b9694-faa5-4b05-b0d6-c72b9694" />
<img width="1070" height="683" alt="Screenshot 2026-01-04 161649" src="https://github.com/user-attachments/assets/a8515831-4804-4642-807c-af4ec4c6ac62" />
<img width="980" height="676" alt="Screenshot 2026-01-04 225958" src="https://github.com/user-attachments/assets/7859627f-5311-4bad-80aa-fc1e6e66e782" />
<img width="1503" height="865" alt="Screenshot 2026-01-04 230618" src="https://github.com/user-attachments/assets/8041fb26-00b8-4548-9958-71e11da5ef94" />
<img width="841" height="729" alt="Screenshot 2026-01-04 232728" src="https://github.com/user-attachments/assets/5afe4b92-18fd-4e19-ae33-f58f580c5d51" />
<img width="919" height="585" alt="Screenshot 2026-01-04 234132" src="https://github.com/user-attachments/assets/8cf72636-ef58-4d5a-857c-0fe3988f7780" />
<img width="1161" height="369" alt="Screenshot 2026-01-04 234142" src="https://github.com/user-attachments/assets/bb0b057f-2871-4009-9771-bc7579a3c3b9" />
<img width="877" height="545" alt="Screenshot 2026-01-05 003420" src="https://github.com/user-attachments/assets/32339c15-a3ee-4802-b5f4-669c75b7e761" />
<img width="856" height="558" alt="Screenshot 2026-01-05 003440" src="https://github.com/user-attachments/assets/c10fd18b-ddc3-433d-9e17-9e2ec0664135" />

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
