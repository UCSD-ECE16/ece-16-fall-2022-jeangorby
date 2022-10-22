int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
bool sending;

unsigned long startTime;
unsigned long currentTime;
unsigned long timeInactive;

void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  sending = false;
  writeDisplay("Sleep", 0, true);
  Serial.begin(9600);
  startTime = millis();
}

void loop() {
  //Commands: off, active, inactive_5, inactive_10
  String command = receiveMessage();
  currentTime = millis();

  if(command == "sleep") {
    sending = false;
    writeDisplay("Sleep", 0, true);
  }
  else if(command == "wearable") {
    sending = true;
    writeDisplay("Wearable", 0, true);
  }
  else if(command == "active"){
    sending = true;
    writeDisplay("Active", 0, true);
  }
  else if(command == "inactive_5"){
    sending = true;
    writeDisplay("Inactive For 5s", 0, true);
  }
  else if(command == "inactive_10"){
    sending = true;
    writeDisplay("Inactive For 10s", 0 , true);
  }

  if(sending && sampleSensors()) {
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);    
  }
}