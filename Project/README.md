# Final Project
Jean Gorby Calicdan A15955623

Haozhang(Jim) Chu A16484292

# Part 1: Space Invaders Controller

## Demo Video
https://youtu.be/CMxRdeafLto 

## Improvements

### Improvement 1: Decoupling Shooting and Moving 

#### Before
The way the game registers both movement and shooting relied on the orientation of the board. This meant that shooting 
and moving at the same time was practically impossible given the way the code is structured to detect orientation. 
#### After
Instead of relying on simply the controllers orientation to shoot and move, we use a button to shoot instead of tracking
through the accelerometer in order to decouple the two actions. This button press is updated more often than movement in
order to ensure all button clicks are registered properly as there are usually a lot more movement commands than shoot 
commands.

![Space Invaders Controller](./images/space%20invaders%20controller.jpg)

### Improvement 2: Smoother Movement 

#### Before
The games orientation detection required super strict tilt since it required one axis to be max in order to detect it

#### After
Instead of checking for absolute orientation, we calculate the tilt degree using math. It starts by setting a reference 
point (reference acceleration values) for the board in order to make sure that it can work if it starts in some other 
orientation than flat. We take incoming acceleration values and subtract them from our reference point. We check both 
the x-axis angle and the y-axis angle. In order to do this, we take the L2 norm between the other two axis we aren't 
observing, (for example, when checking x axis, find L2 norm between y and z), and then taking the incoming value and 
dividing it by this L2 norm. In order to find the angle, we take the ```atan()``` of this value and multiply it by 180 
in order to get the value in degrees. 

### Improvement 3: Removed the Need for Keyboard 

#### Before
In order to start the game, the ```spaceinvaders.py``` file and the ```space_invaders_controller.py``` must be started. 
The player must start the game by clicking a button on their keyboard and if they want to quit the game they must hit 
escape

#### After
The game still requires the two python files to start as usual but we have implemented a way to play the entire game 
without using the keyboard at all as soon as all the python files are ran. In order to start game, the player must click
the shoot button. To exit the game, the player must tilt their controller with the buttons facing opposite of them. 
Consequently, our implementation also ensures that the buffer is always empty when the game starts. Previously, the 
buffer can hold commands even before the game starts which can throw off the players. This is changed because we are 
always waiting for the player input to start the game rather than running the entire while loops all the time before 
the game even starts.

## Features

### Feature 1: Pause/Unpause (Working 100%)
- Placing finger on photodetector will pause the game
- Placing finger on photodetector again wil unpause the game
- One can hit the escape key while paused if they want to exit the game

![pause](./images/pause%20gif.gif)

In order to detect whether a finger is placed on the photodetector, we continously send the ppg data from the ESP32 to 
the python program. When the finger isn't on the photodetector, the PPG value is typically very high (around 32k). 
Placing the finger on the photodetector drops this value down to less than 5k. We check whenever the value drops with 
some room. Whenever this value is reached, with send a "Pause" command to the socket server. This command is interpreted
by the server and calls the ```paused()``` method. <br>

The ```paused()``` method essentially holds the game afloat by keeping it in a while loop. This makes sure that the game
doesn't keep progressing while the game is paused. In this loop, we are looking out for more commands to come in from 
the controller. If we get another "Pause" command, then the game unpauses. We also account for keyboard inputs for the 
keyboard gamers out there. One crucial thing that must be done in this function is to ensure that we are keeping track 
of the time paused. The game code uses a lot of time dependent functions under the hood such as the location of enemy 
ships. Enemy ships are determined by the current time so when paused, it can teleport all the ships to the relevant 
time. In order to avoid this, we keep track of how much time has passed while paused and we subtract this value from the
current time to ensure that all times are synced. <br>

### Feature 2: Changing sensitivity 
- Using a second button, the player can change the sensitivity of the tilt
- Sens option 1 is what we feel is the best, most comfortable sens
- Sens option 2 is the most sensitive we can make it feel without feeling too clunky
- Sens option 3 is the least sensitive we can make it feel, the player has to tilt their controller almost 90 degrees to
- the direction they want to go

Since we made the improvement to our movement system in which we now use tilt angle, it gave us a lot of freedom in 
which ways we can threshold these values to assess in game movement. After messing around with different values, we 
found the best threshold to be around -10 to 60 degrees on the x axis. Note that this is relative to the resting 
position angle which works out to be around 20-30 degrees, rather than zero so it was important to do testing and not 
just use arbitrary numbers. This freedom allowed us to mess with varying levels of sensitivity options to the point 
which gave us the opportunity to allow for different sensitivity profiles. Option 2 is the most sensitive we make it 
without feeling too sensitive. This can be a playstyle for someone who require more precision and is able to control 
the controller well. The last option is a throwback option to how the controller was originally programmed and detected
orientation. The thresholds set for this profile essentially only allows super strict and absolute orientations.

![Second Button](./images/second%20button.jpg)

In order to account for each sensitivity profile, we have created a numpy array which stores all the sensitivity 
thresholds we have as ```sens = np.array([[-10, 60],[0,40],[-200,200]])```. We have also connected a second button on 
the ESP32 side of things which will send a message to python whenever it is clicked. When Python receives this message,
it will cycle through the next set of sensitivity thresholds using array indexing. 

### Feature 3: Vibration Upon Hit 
- Whenever a player gets hit, the arduino will buzz the buzzer motor

In order to implement this feature, we had to go into the game code and find which function handles the player get hit 
by an enemy spaceship which happens to be in the ```check_collisions()```. Within this function, we are establishing a
socket connection between the socket client and the server. When a player is hit, the Socket server will send a "HIT" 
response back to the Socket client. When the client receives this, it sends a "HIT" message to the arduino. The arduino
will then interpret this as its turn to buzz the motor for a second.

## How to use the controller

1. Start the ```spaceinvaders.py``` python program as this is responsible for starting the game and establishing the 
socket server that the controller must connect to
2. Ensure that the proper controller code is uploaded onto the ESP32 board
3. On another terminal, start the ```space_invaders_controller.py``` program in order to start the controller and 
establish it as a client to the socket server
4. In order to start playing the game, the user can simply click the shoot button (left button) on the controller
5. The user can tilt the controller sideways in the direction they want the spaceship to go
6. The user can cycle through different sensitivity profiles by clicking the second button (right button) on the 
controller
7. In order to shoot, the user must click on the shoot button 
8. If the user want to pause the game, they can place their finger on the photodetector and unpause by placing their 
finger back on the photodetector
9. In order to quit the game, the user can tilt the controller forwards (towards the game) and it will stop the game 
program
10. Enjoy the game!

# Part 2: Design Challenge

## YouTube Video Link:


## Need Discussion:
### What is the use case that you are trying to address?
Distraction is a part of the human existence and is inevitable for most humans. Many times distraction can be a good 
thing especially after a full day of nonstop work. The change of scenery as a result of distraction is often what humans
need to relax and enjoy a change of pace. However, distraction could also mean disruption and it can even mean the 
difference between life and death.

### Why is this problem worth addressing?
Case 1: Many people have the habit of texting while driving <br>
"According to the National Safety Council, mobile use while driving leads to 1.6 million accidents every year" <br>

Case 2: In the day and age of the pandemic, online exams have been more prevalent <br>
With that comes the greater number of people cheating on their exams. Online proctoring become a result of the 
transition to online but many times it is handled by few people who would watch over many students and it is easy to 
miss a few people cheating. <br>

Case 3: As a student, it is incredibly easy to lose time and sleep due to distraction <br>
Many times, distraction helps to boost procrastination levels as it is easy to find yourself doing something other than 
working.

### Who is the intended users?
- Car Manufacturers
- Professors
- Teaching Assistants
- Students
- Workers

### How is your solution addressing the need of the user?
Our solution provides a way to detect distraction. For drivers, this provides a way for distraction to be detected and 
minimized while they are driving. For professors and teaching assistants, they are given an automated way to detect 
whether a student is distracted with an unauthorized tool while taking an exam. For students, it allows for direct 
feedback that they are distracted so that they can tell they are distracted because often people get distracted without 
really knowing it.

## Solution Discussion:

### Finite State Diagram
![Finite State Diagram](./images/ECE%2016%20Design%20Challenge%20state%20diagram.jpg)

### What did you choose?
We decided to come up with a way to detect phone distraction which was hardware based by implementing a phone detector. The product is based upon the following pieces of hardware: ESP32CAM board, ESP32 main board, OLED screen, a button, and a buzzer motor. The ESP32CAM board is special and different from the regular ESP32 board that we have been working with throughout the quarter because it allows itself to become an access point which can transmit the video feed coming from the camera. Since it has now become an access point, we can easily program our Python code to "access" it and read the video feed. In Python, we utilize the dnn_DetectionModel from OpenCV with an object recognition model which was been pre-trained. The model is trained with the popular Coco dataset which is vast dataset containing many different images and labels. With the model instantiated, the camera feed from the ESP32CAM is fed into this model and its job is to perform object detection. In order to ensure that there are no duplicates and the best possible option is chosen to detect objects, we do some Non-Maximum Suppression or NMS on the output. When the model is in doubt regarding which label to give an object, it will automatically choose between which one has a higher confidence value. This is what is responsible performing accurate classification on the video feed and detecting whether a phone is in sight. If a phone is within the view, the programm will send "detected" or "undetected" messages to the ESP32 which is displayed on the OLED screen. The ESP32 main board will interpret this and send a HIGH voltage signal to the ESP32 if phone is detected and LOW otherwise. In response, the ESP32CAM will buzz the buzzer accordingly. We have installed a button which can turn off the feature.

### Why did you choose it?
In all the cases we have established earlier, the phone is one of the most common denominator between them all. Texting 
while driving is one of the leading causes of incidents. Cheating on a test is made easier with phones as students can 
easily pull out their phone and either communicate with others or use unauthorized tools such as notes during a closed 
notes exam. Students are very easily distracted by their phone whenever they are working due to the increasing influence
of social media amongst other things.

It was crucial for us to use the ESP3CAM within our design because it was important that our product was mostly hardwar so it doesn't rely on the user's own technology. It's size was important as well as it was small enough to be installed with existing setups such as the rearview mirror of the car or within a students desk.

### What was your thought process in the design?
Our first draft of the design focused on simply making a distraction detector for a student that keeps track of their study environment and checks whether a phone was detected. This is precisely what prompted the design decision to purchase an ESP32CAM and build around it. Later on, we realized that there were more general use cases that can benefit from having a device which can detect phone. We considered the use case of test proctoring. Given the size of the device that we considered earlier, it is easy to utilize our device within a test environment for smart proctoring of an exam. If a student were to pull out their phone during the exam, which is most definitely a breach in academic integrity, then the buzzer will ring to warn whoever is administering the exam. Going back to the idea of the car accidents which have been mentioned throughout the document, the use case of bringing the device into the car to detect driver distraction is now also possible. There is the possibility of selling this device to car manufacturers in order for them to install within their cars can help mitigate car accidents. Our device will warn the driver to look ahead into the road rather than looking at their phone. If a car manufacturer were to install the product, it is likely that consumers are more likely to buy a car for this company as this is a compelling safety feature.

# Division of Labor

## Part 1: Space Invaders Controller
Improvement 1: Decoupling Shooting and Moving     - Haozhang(Jim) Chu <br>

Improvement 2: Smoother Movement                  - Jean Gorby Calicdan  <br>

Improvement 3: Removed the Need for Keyboard      - Jean Gorby Calicdan <br>

Feature 1: Pause/Unpause                          - Jean Gorby Calicdan <br>

Feature 2: Changing Sensitivity                   - Haozhang(Jim) Chu <br>

Feature 3: Vibration Upon Hit                     - Haozhang(Jim) Chu <br>

Recording the video - Jean Gorby Calicdan <br>

## Part 2: Design Challenge

Purchasing an ESP32CAM board                      - Both <br>

Modifying the esp32 cam library                   - Both <br>

Debugging ESP32CAM video feed                     - Both <br>

Setting up access point and WiFi server           - Haozhang(Jim) Chu <br>

Finite State Machine development                  - Haozhang(Jim) Chu <br>

OpenCV dnn_DetectionModel                         - Haozhang(Jim) Chu <br>

OpenCV NMS algorithm                              - Jean Gorby Calicdan <br>

Phone detection added to object detector          - Haozhang(Jim) Chu <br>

Coding and debugging of Bluetooth_receiver (ESP32 SparkFun)  - Haozhang(Jim) Chu <br>

Syncing up ESP32Cam and ESP32                     - Jean Gorby Calicdan <br>

Recording the video - Haozhang(Jim) Chu (presenting) Jean Gorby Calicdan (filming) <br>
