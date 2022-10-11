void setup() {
    setupDisplay();
    // Serial.begin(9600);
}
void loop() {
    // Serial.println("Board works");
    writeDisplay("Display on Row 0", 0, true);
    delay(1000);
    writeDisplay("Display on Row 1", 1, false);
    delay(1000);
    writeDisplay("Display on Row 2", 2, false);
    delay(1000);
    writeDisplay("Cleared Display", 0, true);
    delay(1000);
}