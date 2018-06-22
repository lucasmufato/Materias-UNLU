//pines para los motores
const byte IN1=11;
const byte IN2=10;
const byte IN3=6;
const byte IN4=5;

//constante de velocidad
const int full=255;

//variable para el seguidor de linea
const byte pinSeguidorLinea = A0;
const byte blanco = 0;
const byte negro = 1;

//variables para el ultrasonido
const byte trigPin = 12;
const byte echoPin = A5;
const byte distanciaMinima=50; //es aproximadamente 50cm


//variable para iniciar/detener ataques
const byte boton = 3;
const byte ledVerde = 2;
const byte ledRojo = 8;
volatile boolean standBy;

//manejo del arma
#include <Servo.h>
Servo servo;
const byte pinServo = 9;
const byte distanciaUso=5;
const byte minRange=0;
const byte maxRange=90;
byte posicionArma;

void setup() {
  Serial.begin(9600);
  
  //pines para los motores
  pinMode(IN1,OUTPUT);
  pinMode(IN2,OUTPUT);
  pinMode(IN3,OUTPUT);
  pinMode(IN4,OUTPUT);
  //pin seguidor de linea
  pinMode(pinSeguidorLinea,INPUT);
  //pines para sensor distancia por ultrasonido
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT);
  //pines para leds y variable de control interno
  standBy = true;
  pinMode(ledVerde,OUTPUT);
  pinMode(ledRojo,OUTPUT);
  //escucho por interrupciones generadas cuando se aprieta el boton que altera esta estado del robor( cambia variable standBy)
  attachInterrupt(digitalPinToInterrupt(boton), apretoBoton, RISING);
  //indico a la libreria del servo el pin a utilizar
  servo.attach(pinServo);
  //preparo el arma
  posicionArma=minRange;
  servo.write(posicionArma);
}

void apretoBoton(){
  standBy = !standBy;
  detener();
//  digitalWrite(ledRojo,standBy);
}

void probarseguidor(){
  int piso = digitalRead(pinSeguidorLinea);
  Serial.println(piso==blanco? "blanco":"negro");
  delay(500);
}

void loop() {
//    algo();
  andar();
//probarseguidor();
//delay(1000);
//Serial.println("aa");
}

void algo(){
  delay(100);
  int a = digitalRead(boton);
  Serial.println(a);
  if (a == HIGH){
    digitalWrite(ledRojo,HIGH);
    digitalWrite(ledVerde,LOW);
  }else{
    digitalWrite(ledVerde,HIGH);
    digitalWrite(ledRojo,LOW);
  }
}

void andar(){
  
  if(!standBy){
    //modo de pelea
    Serial.println("atacking");
    digitalWrite(ledRojo,HIGH);
    digitalWrite(ledVerde,LOW);
//    delay(1000);
    int dist=medirDistancia();
    int piso=leerPiso();
    Serial.println(piso==blanco? "blanco":"negro");
    Serial.println(dist);
    if(piso == blanco){
      //si sigo dentro de la plataforma
      if(dist<distanciaMinima){
        //enemigo enfrente
        Serial.println("foward");
        avanzar(full);
//        if(dist<distanciaUso){
//          posicionArma = posicionArma==minRange ? maxRange : minRange;
//          servo.write(posicionArma);
//          delay(25);
//        }
      }else{
        Serial.println("rotate");
        rotarDerecha(full);
      }
    }else{
      //si me estoy por caer
      Serial.println("stop");
      detener();
      delay(50);
      Serial.println("back");
      retroceder(full);
      delay(1000);
      detener();
    }
  }else{
    //modo de espera
    detener();
    delay(100);
    Serial.println("waiting");
    digitalWrite(ledVerde,HIGH);
    digitalWrite(ledRojo,LOW);
  }
  
//  if( dist < distanciaMinima ){
//    Serial.println(piso==blanco? "blanco":"negro");
//    if( piso == negro ){
//      detenerse();
//      retroceder(full);
//      delay(1000);
//      detenerse();
//      delay(50);
//      girarDerechaAdelante(full);
//    }
//  }else{
//    Serial.println(piso==blanco? "blanco":"negro");
//    rotarDerecha(full);
//  }
}

