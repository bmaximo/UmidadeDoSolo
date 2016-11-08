int ativaSensor = 8;
int Sensor = A0;
int val;
int temp = 1000;
void setup(){
pinMode(ativaSensor, OUTPUT);
Serial.begin(9600);
}
void loop(){
digitalWrite(ativaSensor, HIGH);
val = analogRead(Sensor);
if(val >= 600){
Serial.print("Solo Seco ");
Serial.println(val);
}
if((val > 400)&&(val <= 500)){
Serial.print("Solo Umido ");
Serial.println(val);
}
if((val >= 300)&&(val < 400)){
Serial.print("Super Umido ");
Serial.println(val);
}
if(val < 300){
Serial.print("Submerso ");
Serial.println(val);
}
digitalWrite(ativaSensor, LOW);
delay(temp);
}


