// Specify the LED pin
const int RED = 12;
const int YELLOW = 15;
const int BLUE = 14;

// 1hz -> 1s period
// 5hz -> 0.2s period
// 25hz -> 0.04s period

// Initialize time for LED
unsigned long before_time = millis();

// How long the LED stays on or off
int period;
int on_period;
int off_period;

// Start LED logic as “OFF”
int LED = LOW;
int LED_pin;

void setup() {
  // Setup the LED for output
  pinMode(RED, OUTPUT);
  pinMode(YELLOW, OUTPUT);
  pinMode(BLUE, OUTPUT);

  Serial.begin(9600);

}

void loop() {

//red1Hz();
//blue5Hz();
//yellow25Hz();

//  red2then100();
//  blue200then500();
//  yellow20then20();
}

void red1Hz(){
  digitalWrite(RED, HIGH);
  delay(500);
  digitalWrite(RED, LOW);
  delay(500);
}

void blue5Hz(){
  digitalWrite(BLUE, HIGH);
  delay(100);
  digitalWrite(BLUE, LOW);
  delay(100);
}

void yellow25Hz(){
  digitalWrite(YELLOW, HIGH);
  delay(20);
  digitalWrite(YELLOW, LOW);
  delay(20);
}

void red2then100(){
  digitalWrite(RED, HIGH);
  delay(2000);
  digitalWrite(RED, LOW);
  delay(100);
}

void blue200then500(){
  digitalWrite(BLUE, HIGH);
  delay(200);
  digitalWrite(BLUE, LOW);
  delay(500);
}
void yellow20then20(){
  digitalWrite(YELLOW, HIGH);
  delay(20);
  digitalWrite(YELLOW, LOW);
  delay(20);
}
