// Initialize variable the will hold the time
int counter = 0;

// Initialize the pin connected to the button
int BUTTON_PIN = 12;

// Initialize all the necessary states I will use for the program
bool startState = LOW;
bool pauseState = LOW;
bool resetState = LOW;

// Initialize all the time variables that I need to achieve all tasks
unsigned long startTime;
unsigned long currentTime;
unsigned long elapsedTime;
unsigned long timeWhilePaused;
unsigned long pauseTime;
unsigned long buttonTime;
unsigned long buttonPressTime;

void setup() {
  // Initialize pin mode
  pinMode(BUTTON_PIN, INPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:

  /* Program starts in standby mode where nothing really happens until the button is first clicked.
   * As soon as the button is clicked, necessary variables are reset in order to make sure the program as starting from the beginning.
   */
  if(digitalRead(BUTTON_PIN) == LOW && startState == LOW){
    //Start State transition
    startState = !startState;
    resetState = LOW;
    startTime = millis();
    pauseTime = 0;
    timeWhilePaused = 0;
    delay(500);
  }
  else if(digitalRead(BUTTON_PIN) == LOW && startState == HIGH){
    // Pause State transition
    buttonPressTime = 0;
    buttonTime = 0;
    /* Checks how long the button has been pressed
     * This state is also responsible for keeping track of how long the button has been pressed
     * for the situation in which the user wants to reset the program.
     */
    while(digitalRead(BUTTON_PIN) == LOW){
      buttonTime = millis();
      buttonPressTime = buttonTime - currentTime - timeWhilePaused;
      // Serial.println((String) "Button Press Time = " + buttonPressTime/1000);
    }
    buttonTime = 0;

    // Keeps track of time while paused
    pauseState = !pauseState;
    pauseTime += timeWhilePaused;
    timeWhilePaused = 0;

    delay(500);
  }
  else if(buttonPressTime > 3000){
    // Reset state
    Serial.println("You have stopped the timer");
    startState = LOW;
    pauseState = LOW;
    buttonPressTime = 0;
  }

  // Serial.println((String) "startState = " + startState);
  // Serial.println((String) "pauseState = " + pauseState);
  
  if(pauseState){
    /* In this state, we keep track of time while the program is paused. This value
     * is then used later on to subtract from the total elapsed time to compensate.
     */
    timeWhilePaused = millis();
    timeWhilePaused = timeWhilePaused - currentTime;
    // Serial.println((String) "Time While Paused = " + timeWhilePaused/1000);
  }
  else if(startState){
    /*
     *  In this state, we check the total elapsed time by taking any time pause
     *  and subtracting it from the time referenced before hand using the millis() function
     */
    // Serial.println((String) "Pause time = " + pauseTime/1000);
    currentTime = millis();
    elapsedTime = currentTime - startTime - pauseTime;
    counter = elapsedTime/1000;
    // Serial.println((String) "Elapsed Time = " + elapsedTime%100);
    if(elapsedTime % 100 < 10){Serial.println((String) "Elapsed Time = " + counter);}

  }

}
