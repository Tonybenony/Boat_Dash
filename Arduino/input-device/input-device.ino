int RPMPin = A0;
int RPMVal = 0; 

int TempPin = A1;
int TempVal = 0; 

int BattPin = A2;
int BattVal = 0; 

int OilPin = A3;
int OilVal = 0; 

int PressPin = A4;
int PressVal = 0; 

void setup() {
  Serial.begin(9600);
}
void loop() {

RPMVal = analogRead(RPMPin);
TempVal = analogRead(TempPin);
BattVal = analogRead(BattPin);
OilVal = analogRead(OilPin);
PressVal = analogRead(PressPin);

Serial.print(RPMVal);Serial.print(";");

Serial.print(TempVal);Serial.print(";");

Serial.print(BattVal);Serial.print(";");

Serial.print(OilVal);Serial.print(";");

Serial.print(PressVal);Serial.println(";");

delay(50);
}
