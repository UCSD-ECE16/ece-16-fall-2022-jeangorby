int counter = 0;

int BUTTON_PIN = 12;

bool startState = LOW;
bool pauseState = LOW;
bool resetState = LOW;

unsigned long startTime;
unsigned long currentTime;
unsigned long elapsedTime;

void setup() {
  // put your setup code here, to run once:
  pinMode(BUTTON_PIN, INPUT);
  pinMode(LED_BUILTIN, OUTPUT);

  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(BUTTON_PIN) == LOW){
    startState = !startState;
    startTime = millis();
    Serial.println("You clicked the button");
  }
  else if(digitalRead(BUTTON_PIN) == LOW && startState){
    pauseState = !pauseState;
  }

  if(startTime){
    currentTime = millis();
    elapsedTime = currentTime - startTime;
    Serial.println(elapsedTime);
  }
  else if(pauseState){
    return;
  }


}
