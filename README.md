# car

Build an RC car using cardboard and 3D-printed parts; make it autonomous with Raspberry Pi and Python.


![banner.png](imgs/banner.png)


This repository contains all of the files and documentation you need to build a programmable RC car out of cardboard and 3D-printed parts.


### Contents
- [Project Phases](#project-phases)
- [Materials](#materials)
- [FAQ](#faq)


## Project Phases

There are four phases to this project. Please follow the links below for instructions on completing each phase.

1. [Cardboard parts](design_cardboard/)
2. [3D-printed parts](design_3d_print/)
3. [Cardware assembly](cardware_assembly/)
4. Code (coming soon)


## Materials

|	Part	|	Qty	|
|	----------	|	----------:	|
|	[Servo motor (SG90, 180-degree semi rotation)](https://www.amazon.com/ElectroBot-Micro-Helicopter-Airplane-Controls/dp/B071KJV7DD/ref=sr_1_10?ie=UTF8&qid=1538787825&sr=8-10&keywords=servo+motor)	|	1	|
|	[Servo motor (FS90R, 360-degree continuous rotation)](https://www.amazon.com/FEETECH-FS90R-Pack-Continuous-himalayanelixir/dp/B074BFQC3Q/ref=sr_ph_1?ie=UTF8&qid=1538787875&sr=sr-1&keywords=servo+continuous+rotation)	|	1	|
|	[Battery case holder with on/off switch (for 4xAA)](https://www.amazon.com/gp/product/B075G8XZLM/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)	|	1	|
|	[Batteries (AA)]()	|	4	|
|	[Breadboard (small, approx 2" x 3")](https://www.amazon.com/gp/product/B01IMNVZDC/ref=oh_aui_detailpage_o08_s00?ie=UTF8&psc=1)	|	1	|
|	[USB battery charger](https://www.amazon.com/Anker-PowerCore-Lipstick-Sized-Generation-Batteries/dp/B005X1Y7I2/ref=sr_1_15?ie=UTF8&qid=1538788117&sr=8-15&keywords=anker+usb+battery)	|	1	|
|	[Raspberry Pi 3 Model B/B+](https://www.amazon.com/Raspberry-Pi-RASPBERRYPI3-MODB-1GB-Model-Motherboard/dp/B01CD5VC92/ref=sr_1_5?s=pc&ie=UTF8&qid=1538788150&sr=1-5&keywords=raspberry+pi)	|	1	|
|	[Micro SD card (>=16GB)](https://www.amazon.com/Sandisk-Ultra-Micro-UHS-I-Adapter/dp/B073K14CVB/ref=sr_1_2?s=pc&ie=UTF8&qid=1538788228&sr=1-2&keywords=micro+sd+card+16gb)	|	1	|
|	[LCD screen (3.5")](https://www.amazon.com/gp/product/B01IGBDT02/ref=oh_aui_detailpage_o06_s00?ie=UTF8&psc=1)	|	1	|
|	[Camera for Raspberry Pi](https://www.amazon.com/gp/product/B073RCXGQS/ref=oh_aui_detailpage_o07_s00?ie=UTF8&psc=1)	|	1	|
|	[Cable (8") for Raspberry Pi camera](https://www.adafruit.com/product/1647)	|	1	|
|	[Jumper wires (female-male)](https://www.amazon.com/gp/product/B00W8YDCGA/ref=ppx_yo_dt_b_asin_title_o02_s01?ie=UTF8&psc=1)	|	14	|
|	[Zip ties (4")](https://www.amazon.com/gp/product/B00RV9TFAO/ref=oh_aui_detailpage_o05_s00?ie=UTF8&psc=1)	|	50	|
|	[Wide rubber bands (3.5" x 0.75")](https://www.amazon.com/gp/product/B07DKRP2GY/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)	|	1	|
|	[Binding screws (3/16" x 1-1/2")](https://www.amazon.com/gp/product/B07798GWP5/ref=oh_aui_search_detailpage?ie=UTF8&psc=1)	|	1	|
|	[Washers (M5 - Inner x Outter Diameter: 5x15mm/0.2x0.6inch)](https://www.amazon.com/gp/product/B07MKP54P7/ref=ppx_yo_dt_b_asin_title_o07_s00?ie=UTF8&psc=1)	|	1	|
|	[Body clip pins](https://www.rcplanet.com/traxxas-body-clips-12-tra1834/)	|	4	|
|	[Cardboard (chassis) - SET](design_cardboard/)	|	2	|
|	[Cardstock (body) - SET](design_body/)	|	2	|
|	[3D printed parts - SET](design_3d_print/)	|	4	|


## FAQ

### How long will it take me to complete this project?
It depends on whether you decide to:
- make the cardware parts yourself,
- pay a laser cutting and/or 3D printing service to make the parts for you, or
- (COMING SOON) buy a kit containing all of the parts ready for you to assemble. Assuming you spend 1-2 hours per day on this project, the first option might take you a week. The other two options will let you jump directly to Phase 3, after which you can probably start programming in a day or two.


### What can I do with this car?
- Program the Raspberry Pi to drive the car.
- Take pictures and video while driving.
- Collect images and train a neural network that will allow the car to drive itself along road lane markers.
- Incorporate or train your own image classification library to detect stop signs, pedestrians, and/or cats.
- Add additional hardware, such as distance sensors or even Lidar, to enhance self-driving features.


### I'm a parent/teacher. What can my student(s) learn from this project?
- Python programming
- Machine learning using image processing and neural networks
- 3D modeling and printing
- Basic robotics and car engineering
- Industrial design (e.g. car parts, chassis, and body)


### Am I free to make modifications to the files and code in this repo, and can I share my modifications/ideas with others?
Yes! This is an open source project. You are 100% free to do whatever you want with the stuff in this repo. Your creativity is enthusiastically encouraged. Please refer to the [license](LICENSE) for more details.


### I found some mistakes or I have questions about how to complete a step. Where can I request fixes, ask questions, or submit comments/suggestions?
For help with specific steps in the project or fix requests, please create an Issue (and please follow the template).
For other questions, comments, or suggestions, please email them to opencardware@gmail.com.
