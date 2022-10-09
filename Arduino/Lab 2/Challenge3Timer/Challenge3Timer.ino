int timer = 0;

int BUTTON_PIN = 12;

bool countdownState = LOW;

unsigned long startTime;
unsigned long currentTime;
unsigned long elapsedTime;
unsigned long buttonTime;
unsigned long buttonPressTime;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(BUTTON_PIN) == LOW && countdownState == LOW){
    timer++;
    delay(500);
  }
  Serial.println((String) "Current timer = " + timer);
}
