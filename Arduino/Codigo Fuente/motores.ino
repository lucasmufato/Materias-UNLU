//
//int IN1=8;
//int IN2=9;
//int IN3=7;
//int IN4=8;
//
//void setup() {
//  //pines para los motores
//  Serial.begin(9600);
//  pinMode(IN1,OUTPUT);
//  pinMode(IN2,OUTPUT);
//  pinMode(IN3,OUTPUT);
//  pinMode(IN4,OUTPUT);
//  Serial.println("me prendi");
//  detenerse();
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//  Serial.println("aaaaa");
//  digitalWrite(IN1,HIGH);
//  digitalWrite(IN2,LOW);
//  delay(2000);
////  digitalWrite(IN1,LOW);
////  digitalWrite(IN1,LOW);
////  delay(2000);
////  digitalWrite(IN1,LOW);
////  digitalWrite(IN2,HIGH);
////  delay(2000);
//
//}


void avanzar(int velocidad){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,velocidad);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,velocidad);
}

void detener(){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
}

void retroceder(int velocidad){
  digitalWrite(IN1,velocidad);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,velocidad);
  digitalWrite(IN4,LOW);

}

void girarDerechaAdelante(int grados){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}

void girarDerechaAtras(int grados){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
}

void girarIzquierdaAdelante(int grados){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
}

void girarIzquierdaAtras(int grados){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,LOW);
}

/*
 * ROTAR: implica accionar ambos motores
 */
void rotarIzquierda(int grados){
  digitalWrite(IN1,HIGH);
  digitalWrite(IN2,LOW);
  digitalWrite(IN3,LOW);
  digitalWrite(IN4,HIGH);
}

void rotarDerecha(int grados){
  digitalWrite(IN1,LOW);
  digitalWrite(IN2,HIGH);
  digitalWrite(IN3,HIGH);
  digitalWrite(IN4,LOW);
}

