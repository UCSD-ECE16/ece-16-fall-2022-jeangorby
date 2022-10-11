int ax = 0;
int ay = 0;
int az = 0;


void setup() {
  Serial.begin(9600);
  setupAccelSensor();
}

void loop() {
  readAccelSensor();

  // Send to Serial Plotter. Notice the last print has a newline.
  Serial.print("X Value: ");
  Serial.print(ax);
  Serial.print(",");
  Serial.print("Y Value: ");
  Serial.print(ay);
  Serial.print(",");
  Serial.print("Z Value: ");
  Serial.println(az);

}
