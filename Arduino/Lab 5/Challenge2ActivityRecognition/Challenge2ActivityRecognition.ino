#include <CircularBuffer.h>
CircularBuffer<int,256> axBuffer;     // uses 1377 bytes 
CircularBuffer<int,256> ayBuffer;     // uses 1377 bytes 
CircularBuffer<int,256> azBuffer;     // uses 1377 bytes 

int sampleTime = 0;                   // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0;   // Acceleration (from readAccelSensor())
bool recording;

int buttonPin = 12;

unsigned long currentTime;
unsigned long previousTime;
int processTime = 10;
// // Initialize array to serve as a buffer for data to be sent to Python
// int bufferSize = 512
// String buffer[bufferSize];
// int index = 0;
// states: 
int state = 0;
int step_count = 0;
int jump_count = 0;
String count = "";

void setup() {
  pinMode(buttonPin, INPUT);
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  writeDisplay("Sleep", 0, true);
  recording = true;
  Serial.begin(115200);
  previousTime = millis();
}

void loop() {
  // count = "Step count: " + String(step_count) + ",Jump count: " + String(jump_count);
  // writeDisplayCSV(count.c_str(), 1);
  String response = receiveMessage();
  if(response != "None"){
    writeDisplayCSV(response.c_str(), 1);
  }

  // Sending data after button is pushed
  if(state == 1){
    writeDisplay("Sending", 0, true);
    //Send and receive data to python
    while(!azBuffer.isEmpty()){
      currentTime = millis();
      if(currentTime - previousTime > processTime){
        previousTime = currentTime;
        String response = String(axBuffer.shift()) + "," + String(ayBuffer.shift()) + "," + String(azBuffer.shift());
        // Serial.println(response);
        // Serial.println(azBuffer.available());
        // Serial.println(azBuffer.isEmpty());
        sendMessage(response);
      }
    }
    writeDisplay("Done Sending", 0, true);
    state = 0;
    recording = true;
    sendMessage("71");
  }

  if(digitalRead(buttonPin) == LOW){
    state = 1;
    recording = false;
    // Serial.println("button pushed");
    delay(200);
  }

  if(recording && sampleSensors()){
    axBuffer.push(ax);
    ayBuffer.push(ay);
    azBuffer.push(az);
  }
}