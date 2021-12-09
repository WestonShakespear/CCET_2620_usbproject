//hub.ino
//Weston Shakespear

//pin definitions
int buzzerPin = 9;
int ledPin = 10;
int dataPin = 8;

//led brightness
int b = 100;
//buzzer loudness
int c = 100;

//sensor states
int sensorState = 0;
bool state = true;

//sensor watchdog timer
unsigned long int watchdogLast = 0;
int watchdogDelay = 8000;

unsigned long hbLast = 0;
int hbDelay = 100;

//attaching and removing drive indication
bool usbAttached = false;
bool blink = true;
int blinkToggle = 0;
int blinkCount = 0;

//attaching timer
unsigned long blinkLast = 0;
int blinkDelay = 500;

//alarm timer
bool alarm = false;
bool flip = true;
float i = 0;

unsigned long alarmLast = 0;
int alarmDelay = 500;



void setup() {
  Serial.begin(112500);
}

void loop() {
  if (Serial.available() == true) {
    String x = Serial.readString();

    if (x == "a") {
      //new attached
      usbAttached = true;
      blink = true;

    } else if (x == "r") {
      //removed
      blink = true;

    } else if (x == "x") {
      //all removed
      usbAttached = false;

    }

  } else {

    sensorState = digitalRead(dataPin);
    if (sensorState == 1) {
      watchdogLast = millis();
    }

    if (millis() - watchdogLast > watchdogDelay) {
//       analogWrite(ledPin, b);

      if (state == true) {
        state = false;
        if (usbAttached == true) {
          alarm = true;
          blink = true;
        }
      }
    } else {
      if (state == false) {
        state = true;
        alarm = false;
        blink = false;

        analogWrite(ledPin, 0);
        analogWrite(buzzerPin, 0);
//        Serial.println("return");
      }
//       analogWrite(ledPin, 0);
//       Serial.println(millis() - watchdogLast);
    }

    if (millis() - blinkLast > blinkDelay) {
      if (blink == true) {
        analogWrite(ledPin, blinkToggle*b);
        if (blinkToggle == 0) { blinkToggle = 1; }
        else if (blinkToggle == 1) { blinkToggle = 0; blinkCount++; }

        if (alarm == true) {
        analogWrite(buzzerPin, blinkToggle*b);
        } else {
        if (blinkCount > 3) {
          analogWrite(ledPin, 0);
          blink = false;
          blinkCount = 0;
          blinkToggle = 0;
        }
        }
      }
      blinkLast = millis();
//      Serial.println(millis() - blinkLast);
    }

    if (millis() - alarmLast > alarmDelay) {
      if (alarm == true) {

      }
    }


  }

}
