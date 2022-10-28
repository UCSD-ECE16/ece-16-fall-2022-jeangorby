#include <CircularBuffer.h>
CircularBuffer<int,512> axBuffer;     // uses 2754 bytes 
CircularBuffer<int,512> ayBuffer;     // uses 2754 bytes 
CircularBuffer<int,512> azBuffer;     // uses 2754 bytes 

int sampleTime = 0;                   // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0;   // Acceleration (from readAccelSensor())
bool recording;

int buttonPin = 12;

unsigned long currentTime;
unsigned long previousTime;
int processTime = 20;
// // Initialize array to serve as a buffer for data to be sent to Python
// int bufferSize = 512
// String buffer[bufferSize];
// int index = 0;
// states: 0 == recording data, 1 == sending data
int state = 0;


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
  // Sending data after button is pushed data 
  while(state == 1){
    currentTime = millis();
    //Send and receive data to python
    if(!azBuffer.isEmpty() && currentTime - previousTime > processTime){
      previousTime = currentTime;
      String response = String(axBuffer.shift()) + "," + String(ayBuffer.shift()) + "," + String(azBuffer.shift());
      // Serial.println(response);
      sendMessage(response);
    }
    else if(azBuffer.isEmpty()){
      state == 0;
    }
    String response =  receiveMessage();
    writeDisplay(response.c_str(), 0, true);
  }

  if(digitalRead(buttonPin) == LOW){
    state = 1;
    // Serial.println("button pushed");
    delay(200);
  }

  if(recording && sampleSensors()){
    // sampleSensors();
    // String response = String(sampleTime) + ",";
    // response += String(ax) + "," + String(ay) + "," + String(az);
    axBuffer.push(ax);
    ayBuffer.push(ay);
    azBuffer.push(az);

    // Serial.println(azBuffer.last());
  }
}