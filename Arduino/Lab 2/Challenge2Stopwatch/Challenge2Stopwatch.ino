int counter = 0;

int BUTTON_PIN = 12;

bool startState = LOW;
bool pauseState = LOW;
bool resetState = LOW;

unsigned long startTime;
unsigned long currentTime;
unsigned long elapsedTime;
unsigned long timeWhilePaused;
unsigned long pauseTime;
unsigned long buttonTime;
unsigned long buttonPressTime;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  if(digitalRead(BUTTON_PIN) == LOW && startState == LOW){
    startState = !startState;
    resetState = LOW;
    startTime = millis();
    delay(500);
  }
  else if(digitalRead(BUTTON_PIN) == LOW && startState == HIGH){
    pauseState = !pauseState;
    pauseTime += timeWhilePaused;
    timeWhilePaused = 0;
    delay(500);
  }
  else if(buttonPressTime > 3000){
    Serial.println("You have stopped the timer");
    startState = LOW;
    resetState = HIGH;
  }

  // Serial.println((String) "startState = " + startState);
  // Serial.println((String) "pauseState = " + pauseState);
  
  if(pauseState){
    timeWhilePaused = millis();
    timeWhilePaused = timeWhilePaused - currentTime;
    Serial.println((String) "Time While Paused = " + timeWhilePaused/1000);
  }
  else if(startState){
    Serial.println((String) "Pause time = " + pauseTime/1000);
    currentTime = millis();
    elapsedTime = currentTime - startTime - pauseTime;
    Serial.println((String) "Elapsed Time = " + elapsedTime/1000);
  }
  else if(resetState){
    int i = 0;
  }

      buttonTime = 0;
  while(digitalRead(BUTTON_PIN) == LOW && startState == HIGH){
    buttonTime = millis();
    buttonPressTime = buttonTime - currentTime;
    if(buttonPressTime < 3000 && digitalRead(BUTTON_PIN) == HIGH){
      pauseState = HIGH;
    }
    Serial.println((String) "Button Press Time = " + buttonPressTime/1000);
  }

}
