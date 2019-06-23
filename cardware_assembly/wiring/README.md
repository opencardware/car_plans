# Wiring

### What you'll need

- Raspberry Pi
- microSD card containing Raspbian OS image
- LCD screen (3.5") for Raspberry Pi
- jumper wires (15)


Connect the power (red) and ground (black) wires to the power supply pins on the breadboard.

![IMG_20181218_111947_resized.jpg](imgs_wiring/IMG_20181218_111947_resized.jpg)

Secure them by taping them down.

![IMG_20181218_112453_resized.jpg](imgs_wiring/IMG_20181218_112453_resized.jpg)

Attach male-male jumper wires to the power and ground pins of the two servo motors.

![IMG_20181218_112107_resized.jpg](imgs_wiring/IMG_20181218_112107_resized.jpg)

Feed the wires from the servos through the side of the carriage, like so.

![IMG_20181218_112548_resized.jpg](imgs_wiring/IMG_20181218_112548_resized.jpg)

Plug them into the power supply pins of the breadboard.

![IMG_20181218_112846_resized.jpg](imgs_wiring/IMG_20181218_112846_resized.jpg)

Use a male-female jumper wire to connect the breadboard's ground to the Pi's ground. Locate the ground pins on the Pi using this [site](https://pinout.xyz/#).

![IMG_20181218_112920_resized.jpg](imgs_wiring/IMG_20181218_112920_resized.jpg)

Use male-female jumper wires to extend the servos' signal wires.

![IMG_20181218_113123_resized.jpg](imgs_wiring/IMG_20181218_113123_resized.jpg)

Tuck the breadboard into the carriage.

![IMG_20181218_113225_resized.jpg](imgs_wiring/IMG_20181218_113225_resized.jpg)

Get the LCD screen and 12 male-female jumper wires.

![MVIMG_20190310_143139_resized.jpg](imgs_wiring/MVIMG_20190310_143139_resized.jpg)

This table shows the pin interface for the LCD screen. The LCD normally sits on top of the Pi, covering 26 of the GPIO pins. We're only going to connect the 12 pins we need to make the LCD work with the Pi.

![LCD_pins.jpg](imgs_wiring/LCD_pins.jpg)

The "PIN NO." column lists the 12 pins that need to be connected. Each row in this column lists the pin number(s) on the Pi that can do the job required for that "SYMBOL". (For simplicity's sake, I went with the first number in each row.) Again, you can use this [site](https://pinout.xyz/#) for reference on the Pi's GPIO pin numbers.

![MVIMG_20190310_143657_resized.jpg](imgs_wiring/MVIMG_20190310_143657_resized.jpg)

Use tape to secure the pins in place on the LCD.

![MVIMG_20190310_143921_resized.jpg](imgs_wiring/MVIMG_20190310_143921_resized.jpg)

Feed the wires through LCD mount, like so.

![MVIMG_20190310_144009_resized.jpg](imgs_wiring/MVIMG_20190310_144009_resized.jpg)

Slide the LCD mount into the corresponding mounts on the carriage.

![MVIMG_20190310_144203_resized.jpg](imgs_wiring/MVIMG_20190310_144203_resized.jpg)

Lower the LCD into the mount...

![MVIMG_20190310_144234_resized.jpg](imgs_wiring/MVIMG_20190310_144234_resized.jpg)

...like so.

![MVIMG_20190310_144754_resized.jpg](imgs_wiring/MVIMG_20190310_144754_resized.jpg)

Connect the jumper wires from the LCD into Pi's GPIO pins (should correspond exactly with the pin locations on the LCD).

![MVIMG_20190310_144859_resized.jpg](imgs_wiring/MVIMG_20190310_144859_resized.jpg)

Should look like this when you're done.

![MVIMG_20190310_145224_resized.jpg](imgs_wiring/MVIMG_20190310_145224_resized.jpg)

Plug in the USB battery charger.

![MVIMG_20190310_183959_resized.jpg](imgs_wiring/MVIMG_20190310_183959_resized.jpg)

After inserting the micro SD card with the OS installed, turn on the USB battery to boot up the Pi.

![MVIMG_20190310_145837_resized.jpg](imgs_wiring/MVIMG_20190310_145837_resized.jpg)

Connect to Wi-Fi.

![MVIMG_20190310_182400_resized.jpg](imgs_wiring/MVIMG_20190310_182400_resized.jpg)

Open the Terminal and find out the IP address of your Pi. Use that IP address to SSH into your Pi for easier code editing.

![MVIMG_20190310_182437_resized.jpg](imgs_wiring/MVIMG_20190310_182437_resized.jpg)
