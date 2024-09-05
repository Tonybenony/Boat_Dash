int RPMPin = A3;
int RPMVal = 0; 

int TempPin = A2;
int TempVal = 0; 

int BattPin = A1;
int BattVal = 0; 

void setup() {
  Serial.begin(9600);
}
void loop() {

RPMVal = analogRead(RPMPin);
TempVal = analogRead(TempPin);
BattVal = analogRead(BattPin);

Serial.print(RPMVal);Serial.print(";");

Serial.print(TempVal);Serial.print(";");

Serial.print(BattVal);Serial.println(";");


delay(50);
}
