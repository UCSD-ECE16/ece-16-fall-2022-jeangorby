int sampleTime = 0; // Time of last sample (in Sampling tab)
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; 
int ay = 0;
int az = 0;

int numTaps = 0;

void setup() {
  setupAccelSensor();
  setupDisplay();
  Serial.begin(115200);
}

void loop() {
  readAccelSensor();

  if(sampleSensors() && Serial.availableForWrite()) {
    numTaps += detectTaps();
    String taps = (String)"Taps: " + numTaps;
    Serial.print("X: ");
    Serial.print(ax);
    Serial.print(",");
    Serial.print("Y: ");
    Serial.print(ay);
    Serial.print(",");
    Serial.print("Z: ");
    Serial.println(az);

    writeDisplay(taps.c_str(), 0, false);
  }

}

int detectTaps(){
  if(az < 2400 || az > 2600){
    return 1;
  }
  else
    return 0;
}