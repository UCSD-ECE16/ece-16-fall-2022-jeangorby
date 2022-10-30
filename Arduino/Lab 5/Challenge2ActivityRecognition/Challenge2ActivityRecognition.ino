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
  // Updates the OLED screen when new counts come from Python
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
        // Organize data into one string to send to Python
        String response = String(axBuffer.shift()) + "," + String(ayBuffer.shift()) + "," + String(azBuffer.shift());
        sendMessage(response);
      }
    }
    writeDisplay("Done Sending", 0, true);
    state = 0;
    recording = true;
    sendMessage("71");
  }

  // Check if button has been pushed in order to start the process for sending data
  if(digitalRead(buttonPin) == LOW){
    state = 1;
    recording = false;
    delay(200);
  }

  // Continuously update the buffer unless the MCU is sending data
  if(recording && sampleSensors()){
    axBuffer.push(ax);
    ayBuffer.push(ay);
    azBuffer.push(az);
  }
}