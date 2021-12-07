void setup() {
  Serial.begin(112500);
}

void loop() {
  while (!Serial.available());
  String x = "1" + Serial.readString();
  Serial.println(x);
}
