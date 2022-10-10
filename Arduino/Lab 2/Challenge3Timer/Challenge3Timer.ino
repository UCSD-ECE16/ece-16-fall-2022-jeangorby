// Initialize variable the will hold the time
int counter = 0;

// Initialize the pin connected to the button
int BUTTON_PIN = 12;

// Initialize the one state that I need
bool countdownState = LOW;

// Initialize all the time variables that I need to achieve all tasks
unsigned long startTime;
unsigned long buttonFirstTime;
unsigned long timeSinceLastPush;
unsigned long buttonTime;
unsigned long buttonPressTime;
unsigned long oneSecondClock;
unsigned long seconds;

void setup() {
  // Initialize pin mode
  pinMode(BUTTON_PIN, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  startTime = millis();

  // Dictates how the circuit reacts when a button is clicked
  if(digitalRead(BUTTON_PIN) == LOW){
    // Reset and initialize any variables I need
    timer++;
    buttonFirstTime = millis();
    seconds = millis();
    timeSinceLastPush = 0;
    buttonPressTime = 0;
    buttonTime = 0;
    // Checks how long the button has been held down for
    while(digitalRead(BUTTON_PIN) == LOW){
      buttonTime = millis();
      buttonPressTime = buttonTime - startTime;
      // Serial.println((String) "Button Press Time = " + buttonPressTime);
    }
    delay(500);
  }
  // If the button has been held down for at least 3 seconds, reset the timer
  else if(buttonPressTime > 3000){
    timer = 0;
  }

  // Updates the variables needed to keep track of how much and when to decrement timer
  timeSinceLastPush = startTime - buttonFirstTime;
  oneSecondClock = startTime - seconds;

  // If it has been at least 3 seconds since last click and timer isnt zero, decrement the timer variable
  // once every one second
  if(timeSinceLastPush > 3000 && oneSecondClock > 1000 && timer > 0){
    timer--;
    oneSecondClock = 0;
    seconds = millis();
  }


  // Serial.println((String) "Time Since Last Button Press = " + timeSinceLastPush);
  if(startTime % 100 < 10){Serial.println((String) "Current timer = " + timer);}
  // Serial.println((String) "One Second Clock = " + oneSecondClock);
}
