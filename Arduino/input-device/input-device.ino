void setup() {
  Serial.begin(9600);
}
void loop() {
  int count=0;
  while(count<1560){
    Serial.println(count);
    count++;
    delay(50);
  }
}
