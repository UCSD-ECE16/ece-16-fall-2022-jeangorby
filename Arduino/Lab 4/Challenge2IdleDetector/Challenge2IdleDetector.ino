int sampleTime = 0; // Time of last sample (in Sampling tab)
int ax = 0; int ay = 0; int az = 0; // Acceleration (from readAccelSensor())
bool sending;

int LED_PIN = 21;
int LED = LOW;
int period;
int on_period = 500;
int off_period = 500;

unsigned long start_time;
unsigned long current_time;

void setup() {
  setupAccelSensor();
  setupCommunication();
  setupDisplay();
  setupMotor();
  sending = false;
  writeDisplay("Sleep", 0, true);
  Serial.begin(9600);
  start_time = millis();
  pinMode(LED_PIN, OUTPUT);
}

void loop() {
  //Commands: off, active, inactive_5, inactive_10
  String command = receiveMessage();
  current_time = millis();

  if(command == "off") {
    sending = true;
    writeDisplay("Off", 0, true);
  }
  else if(command == "on"){
    sending = true;
    writeDisplay("On", 0 , true);
  }
  else if(command == "active"){
    sending = true;
    writeDisplay("Active", 0, true);
  }
  else if(command == "inactive_5"){
    sending = true;
    writeDisplay("Inactive For 5s", 0, true);
    if(current_time - start_time >= period){
      start_time = millis();

      if(LED == LOW){
        LED = HIGH;
        period = on_period;
      }
      else{
        LED = LOW;
        period = off_period;
      }
    }
    digitalWrite(LED_PIN, LED);

  }
  else if(command == "inactive_10"){
    digitalWrite(LED_PIN, LOW);
    sending = true;
    writeDisplay("Inactive For 10s", 0 , true);
    Serial.println(current_time - start_time);
    if(current_time - start_time < 1500){
      activateMotor(255);
    }
    else{
      deactivateMotor();
    }
  }

  if(sending && sampleSensors()) {
    String response = String(sampleTime) + ",";
    response += String(ax) + "," + String(ay) + "," + String(az);
    sendMessage(response);    
  }
}