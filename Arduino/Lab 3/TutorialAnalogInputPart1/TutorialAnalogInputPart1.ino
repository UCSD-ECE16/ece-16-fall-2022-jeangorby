const int accelX = A2;

void setup() {
  // Begin the Serial communication (you did this in the last lab!)
  Serial.begin(9600);
  // Define the analog pin as input
  pinMode(accelX, INPUT);

}

void loop() {
  int accel_val = analogRead(accelX);
  // Print the value (you did this in the last lab too)
  Serial.println(accel_val);

}
