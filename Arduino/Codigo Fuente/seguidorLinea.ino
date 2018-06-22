//const int pinSeguidorLinea = A10;
//const int blanco = 0;
//const int negro = 1;

//void setup() {
//  Serial.begin(9600);
//  pinMode(pinSeguidorLinea,INPUT);
//}
//
//void loop() {
//  int lectura = digitalRead(pinSeguidorLinea);
//  Serial.println(lectura);
//  delay(500);
//}

int leerPiso(){
  return digitalRead(pinSeguidorLinea);
}

