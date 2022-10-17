#include <Smoothed.h>
Smoothed <float> mySensor;

int sampleTime = 0; // Time of last sample (in Sampling tab)
// Acceleration values recorded from the readAccelSensor() function
int ax = 0; 
int ay = 0;
int az = 0;

// All possible states
const int RESET = 0;
const int COUNTDOWN = 1;
const int BUZZ = 2;

int state;
bool resetFlag = false;
bool buzzerOn;

int numTaps = 0;

unsigned long startTime;
unsigned long currentTime;
unsigned long tapTime;
unsigned long fiveTimer;
unsigned long secondsTimer;
unsigned long timeInFunction;

void setup() {
  mySensor.begin(SMOOTHED_AVERAGE, 10);

  setupAccelSensor();
  setupDisplay();
  setupMotor();
  Serial.begin(115200);

  state = RESET;
  startTime = millis();
}

void loop() {
  readAccelSensor();
  mySensor.add(analogRead(A4));

  // if(sampleSensors() && Serial.availableForWrite()) {
  //   numTaps += detectTaps();
  //   String taps = (String)"Taps: " + numTaps;
  //   Serial.print("X: ");
  //   Serial.print(ax);
  //   Serial.print(",");
  //   Serial.print("Y: ");
  //   Serial.print(ay);
  //   Serial.print(",");
  //   Serial.print("Z: ");
  //   Serial.println(az);
  //   Serial.println(mySensor.get());
  //   if(mySensor.get() != 2545.00)
  //     Serial.println("a;sldkfhaskldjfhaskdjfhaksdjfhkasjdhfkjasdhfkjahsdf");

  //   writeDisplay(taps.c_str(), 2, false);
  // }

  Serial.println((String)"State: " + state);
  String taps = (String)"Taps: " + numTaps;
  switch(state){
    case RESET:
    currentTime = millis();
    fiveTimer = currentTime - startTime;
    // Serial.println((String)"FiveTimer: " + fiveTimer);
      if(detectTaps(startTime, currentTime) == 2){
        numTaps = 0;
        state = BUZZ;
        Serial.println("asdfasdfqwerqwerqwerasdfasdfasdf");
        delay(2000);
      }
      else if(sampleSensors() && detectTaps(startTime, currentTime) != 0){
        numTaps += 1;
        startTime = currentTime;
      }
      else if(fiveTimer > 5000){
        state = COUNTDOWN;
        startTime = currentTime;
      }
      else if(resetFlag){
        resetFlag = false;
        numTaps = 0;
        state = BUZZ;
      }
      writeDisplay(taps.c_str(), 0, true);
      break;
    case COUNTDOWN:
    currentTime = millis();
    secondsTimer = currentTime - startTime;
    // Serial.println((String)"Seconds: " + secondsTimer);
      if(detectTaps(startTime, currentTime) == 2){
        numTaps = 0;
        state = BUZZ;
        // delay(1000);
      }
      else if(sampleSensors() && detectTaps(startTime, currentTime) == 1){
        numTaps += 1;
        state = RESET;
      }
      else if(secondsTimer > 1000){
        numTaps -= 1;
        startTime = currentTime;
      }
      else if(resetFlag || numTaps == 0){
        resetFlag = false;
        startTime = currentTime;
        state = BUZZ;
      }
      writeDisplay(taps.c_str(), 0, true);
      break;
    case BUZZ:
      // turn the buzzer on
      if(sampleSensors() && detectTaps(startTime, currentTime) == 0){
        // activateMotor(255);
        buzzerOn = true;
      }
      else if(detectTaps(startTime, currentTime) != 0){
        // deactivateMotor();
        numTaps += 1;
        state = RESET;
        startTime = currentTime;
      }
      writeDisplay(taps.c_str(), 0, true);
      break;
    default:
      state = RESET;
      break;
  }

}

int detectTaps(unsigned long startTime, unsigned long currentTime){
  if(mySensor.get() < 2530){
    if(az < 2400 || az > 2600){
      return 1;
    }
    else{
      return 0;
    }
  }

  timeInFunction = 0;
  while(mySensor.get() > 2600){
    // Serial.println(mySensor.get());
    timeInFunction = millis();
    Serial.println(timeInFunction - startTime);
    if(timeInFunction - startTime > 2000){
      timeInFunction = 0;
      // delay(1000);
      startTime = 0;
      return 2;
    }
    else{
      startTime = 0;
      return 0;
    }
  } 

}