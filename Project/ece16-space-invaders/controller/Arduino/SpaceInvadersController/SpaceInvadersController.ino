/*
 * Global variables
 */
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; int ay = 0; int az = 0;
int ppg = 0;        // PPG from readPhotoSensor() (in Photodetector tab)
int sampleTime = 0; // Time of last sample (in Sampling tab)
bool sending;

int BUTTON_PIN = 15;
int button_now_state;                  //current state of button1
int button_pre_state = HIGH;           //previous state of button1

int SENS_BUTTON = 16;
int button2_now_state;                  //current state of button2
int button2_pre_state = HIGH;           //previous state of button2

String response = "";

/*
 * Initialize the various components of the wearable
 */
void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupPhotoSensor();
  pinMode(BUTTON_PIN, INPUT);
  pinMode(SENS_BUTTON, INPUT);
  sending = false;
  Serial.begin(115200);
  writeDisplay("Ready...", 1, true);
  writeDisplay("Set...", 2, false);
  writeDisplay("Play!", 3, false);
}

/*
 * The main processing loop
 */
void loop() {
  // Parse command coming from Python (either "stop" or "start")
  String command = receiveMessage();
  button_now_state = digitalRead(BUTTON_PIN);         //getting the current button state
  button2_now_state = digitalRead(SENS_BUTTON);         //getting the current button state
  sending = true;
  if(command == "stop") {
    sending = false;
    writeDisplay("Controller: Off", 0, true);
  }
  else if(command == "start") {
    sending = true;
    writeDisplay("Controller: On", 0, true);
  }

  // Send the orientation of the board
  if(sending && press_checker()){
    response = "0,0,0,-1";
    sendMessage(response);
  }
  else if(sending && press_checker2()){
    response = "0,0,0,-2";
    sendMessage(response);
  }
  else if(sending && sampleSensors()) { 
    response = String(ax) + "," + String(ay) + "," + String(az) + "," + String(ppg);
    sendMessage(response);
  }
}

int press_checker() {
  if (button_pre_state == button_now_state) {         //no transition occurs
    if (button_now_state == HIGH){                     
    }
    else { //button1_now_state == LOW                   //if the button stays LOW there is a possible chance to reach 3s worth resetting
    }
    button_pre_state = button_now_state;              //updating the button state
    return 0;
  }
  else {  //button_pre_state != button_now_state        //transition occurs
    if (button_now_state == HIGH){                     //transition from LOW to HIGH consider pressed
      button_pre_state = button_now_state;            //updating the button state
      return 1;
    }
    else { //button1_now_state == LOW                   //transition from HIGH to LOW not consider pressed
      if(button_pre_state == HIGH){
      }
      button_pre_state = button_now_state;            //updating the button state
      return 0;
    }
  }
}

int press_checker2() {
  if (button2_pre_state == button2_now_state) {         //no transition occurs
    if (button2_now_state == HIGH){                     
    }
    else { //button2_now_state == LOW                   //if the button stays LOW there is a possible chance to reach 3s worth resetting
    }
    button2_pre_state = button2_now_state;              //updating the button state
    return 0;
  }
  else {  //button2_pre_state != button_now_state        //transition occurs
    if (button2_now_state == HIGH){                     //transition from LOW to HIGH consider pressed
      button2_pre_state = button2_now_state;            //updating the button state
      return 1;
    }
    else { //button2_now_state == LOW                   //transition from HIGH to LOW not consider pressed
      if(button2_pre_state == HIGH){
      }
      button2_pre_state = button2_now_state;            //updating the button state
      return 0;
    }
  }
}

