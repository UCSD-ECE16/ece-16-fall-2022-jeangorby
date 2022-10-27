int sampleTime = 0;                   // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0;   // Acceleration (from readAccelSensor())
bool sending;

int buttonPin = 13;

// Initialize array to serve as a buffer for data to be sent to Python
int bufferSize = 512
String buffer[bufferSize];
int index = 0;
// states: 0 == recording data, 1 == sending data
int state = 0;


void setup() {
  pinMode(buttonPin, INPUT);
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  sending = false;
  writeDisplay("Sleep", 0, true);
}

void loop() {
  // String command = receiveMessage();
  // if(command == "sleep") {
  //   sending = false;
  //   writeDisplay("Sleep", 0, true);
  // }
  // else if(command == "wearable") {
  //   sending = true;
  //   writeDisplay("Wearable", 0, true);
  // }
  // else{
  //   writeDisplay(command.c_str(), 2, false);
  // }
  // if(sending && sampleSensors()) {
  //   String response = String(sampleTime) + ",";
  //   response += String(ax) + "," + String(ay) + "," + String(az);
  //   sendMessage(response);    
  // }

  // Recording data 
  if(state == 0){
    sampleSensors();
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    // Record only until buffer is full
    // If buffer is full, then prompt user to click button
    if(index != bufferSize - 1){
      buffer[index] = response;
    }
    else if{
      Serial.println("Buffer is full. Please press the button");
    }
  }
  else if(state == 1){
    //Send and receive data to python
    for(int i = 0, i<bufferSize, i++){
      sendMessage(buffer[i])
    }
    String response =  receiveMessage();
    writeDisplay(response.c_str(), 0, true);
  }

  if(digitalRead(buttonPin) == LOW){
    state = 1;
  }
}