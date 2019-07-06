const float refVolt = 1.1;
const int Analpin = 0;

void setup() {
  // put your setup code here, to run once:
analogReference(INTERNAL);
Serial.begin(115200);
}

void loop() {
  //put your main code here, to run repeatedly:
  int val = analogRead(Analpin);
  float mVolts = (val / 1.023) * refVolt;
Serial.println(mVolts);

delay (1000);

}
