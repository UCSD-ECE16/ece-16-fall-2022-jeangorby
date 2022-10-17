String row1 = "";
String row2 = "";
String row3 = "";
String row4 = "";

int counter = 0;

void setup() {
  Serial.begin(115200);
  setupCommunication();
  setupDisplay();
}

void loop() {
  String message = receiveMessage();
  if(message != "") {
    row1 = message;
    counter++;
  }
  else if (message != "" && counter == 1){
    row2 = message;
    counter++;
  }

  writeDisplay(row1.c_str(), 0, true);
  writeDisplay(row2.c_str(), 1, true);

}