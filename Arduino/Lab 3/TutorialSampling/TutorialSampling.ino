int sampleTime = 0; // Time of last sample (in Sampling tab)
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; 
int ay = 0;
int az = 0;


void setup() {
  // put your setup code here, to run once:
  setupAccelSensor();
  setupDisplay();
  Serial.begin(115200);

}

void loop() {
  // put your main code here, to run repeatedly:
  // Note: we only print values when we have a new sample!!!
  // Also note that we added the second argument to the conditional to    
  // check if there is space in the buffer, otherwise it will stall when 
  // the buffer is full. Credit to Kyle for discovering the solution!
  if(sampleSensors() && Serial.availableForWrite()) {
      Serial.print("X Value: ");
      Serial.print(ax);
      Serial.print(",");
      Serial.print("Y Value: ");
      Serial.print(ay);
      Serial.print(",");
      Serial.print("Z Value: ");
      Serial.println(az);
  }

}
