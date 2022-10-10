int timer = 0;

int BUTTON_PIN = 12;

bool countdownState = LOW;

unsigned long startTime;
unsigned long buttonFirstTime;
unsigned long timeSinceLastPush;
unsigned long buttonTime;
unsigned long buttonPressTime;
unsigned long oneSecondClock;
unsigned long seconds;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  startTime = millis();
  if(digitalRead(BUTTON_PIN) == LOW && countdownState == LOW){
    timer++;
    buttonFirstTime = millis();
    seconds = millis();
    timeSinceLastPush = 0;
    buttonPressTime = 0;
    buttonTime = 0;
    while(digitalRead(BUTTON_PIN) == LOW){
      buttonTime = millis();
      buttonPressTime = buttonTime - startTime;
      Serial.println((String) "Button Press Time = " + buttonPressTime);
    }
    delay(500);
  }
  else if(buttonPressTime > 3000){
    timer = 0;
  }

  timeSinceLastPush = startTime - buttonFirstTime;
  oneSecondClock = startTime - seconds;

  if(timeSinceLastPush > 3000 && oneSecondClock > 1000 && timer > 0){
    timer--;
    oneSecondClock = 0;
    seconds = millis();
  }


  // Serial.println((String) "Time Since Last Button Press = " + timeSinceLastPush);
  if(startTime % 100 < 30){Serial.println((String) "Current timer = " + timer);}
  // Serial.println((String) "One Second Clock = " + oneSecondClock);
}
