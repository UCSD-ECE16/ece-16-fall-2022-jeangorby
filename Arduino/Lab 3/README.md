Jean Gorby Calicdan
A15955623

# Lab #3

# Tutorial Review
## Tutorial 1: I2C Communication & OLED Display
The OLED display is a great way for users to interface with the microcontroller rather than just relying on simply print statements. The OLED display we use for this course uses I2C communication, in which we include the Wire library in order to take care of most of it for us. Wiring the OLED screen is as simple as wiring any other components but it does use special ports on ESP32 such as the **SCL** and the **SDA** ports. In order to make the OLED display code modular, so that it can easily be ported over to future programs, it is necessary to create a new tab in which a lot of the setup and desired functions will already be taken care of. Displaying any text to the OLED screen is now as simple as calling the ```writeDisplay()``` function.

## Tutorial 2: Analog Input (Accelerometer)
An accelerometer is a sensor which exist in very many of the technologies that humans use in their day to day basis. The accelerometer we use is analog in the sense that it produces continuous data but in order to utilize, we must convert it to digital using an ADC. Depending on the resolution of the ADC, the output can be represented in may ways. In terms of wiring the accelerometer, it is pertinent that we use the analog ports in order to interface with each axis value. The values can then be displayed by printing them and utilizing Arduino IDE's Serial Plotter. Similar to the display, we created another tab to take care of the accelerometer to make it easier to use in future programs.

## Tutorial 3: Analog Output (PWM)
Pulse Width Modulation is a way to use digital values in order to produce an analog output. This is done by having an on/off cycle with varying frequencies in order to produce a sense of dimness. For instance, if an LED were to be turned on/off equally repeatedly, it gives the sense that the LED is about halfway turned on. In the arduino IDE, there are built in functions which help create PWM output which can be used for either LEDs or even buzzer motors. Like the two previous tutorials, a motor tab was created in order to modularize powering the motor with PWM.

## Tutorial 4: Sampling
Sampling is a way for us to make our lives easier when dealing with analog inputs because it allows for the digitizing of these massively varying inputs. Depending on how well we sample it, i.e. the sampling rate that we choose, one can operate on analog signals much less chaotically. A sampling tab will be created for this tutorial. The accelerometer from earlier is a great example of an analog input which can be sampled and analyzed. By taking the tabs from earlier and even integrating the OLED display, we can create a program that uses a bunch of technologies to accomplish a task cleanly.

## Tutorial 5: Python Serial & BT Communication
The ESP32 is entirely capable of communicating in many ways, two of which include communicating directly with Python and even through Bluetooth (or both!). The PySerial library will be needed in order for this to work. This library allows us to send and even receive data, essentially communicate, between Python and the microcontroller unit. Bluetooth works in a very similar sense but this time, we are not tethered by a wire connected to the computer that we are communicating with. It is important to distinguish within the sketch uploaded to MCU which method of communication we are using in order to not cause any confusion. This can be done by using precompiler directives such that we can simply change one variable in order to switch between the Serial or Bluetooth connections.

# Challenges

## Challenge 1: Gesture Detection
In order to detect taps, we must observe what it looks like when a tap is made within the serial plotter. <br>
![tap](.\images\tap.png) <br>
One can see that when a tap is made, the az values drop down significantly. One can also see the same value goes up when it bounces up. I have also found instances in which the value goes up rather than down when a tap is made. Therefore, I made sure to account for both without the possibility of double counting by creating a proper conditional statement for it. <br>

## Challenge 2: Gesture-Controlled Watch


## Challenge 3: Wireless Weather Watch
