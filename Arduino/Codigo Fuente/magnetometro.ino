//
//#include "Wire.h"
//#include "HMC5883L.h"
//#include "I2Cdev.h"
//
//HMC5883L magnetometro;
//
//int16_t mx, my, mz;
//void setup() {
//    Serial.begin(9600);
//    Serial.println("Inicializando Magnetometro...");
//    //Inicializamos la comunicación I2C y el magnetómetro
//    Wire.begin();
//    magnetometro.initialize();
//}
//
//void loop() {
//    //Obtenemos del magnetometro las componentes del campo magnético
//    magnetometro.getHeading(&mx, &my, &mz);
//    
//    Serial.print("mx:");
//    Serial.print(mx); 
//    Serial.print("\tmy:");
//    Serial.print(my);
//    Serial.print("\tmz:");
//    Serial.println(mz);
//    delay(100);
//}
//

//
// Código brújula digital con sensor magnetometro HMC5883
// Basado en el código de http://www.ardumania.es/brujula-digital-hmc5883l/
//
// Añadi LEDs para que indiquen la dirección y así no depender
// del monitor Serial.
//
// 
//#include <Wire.h>
//#include <HMC5883L.h> //Include a biblioteca HMC5883L.h
//#include <Adafruit_HMC5883_U.h>
// 
//HMC5883L brujula; //Instância a biblioteca para a bússola
// 
//int i; //Variable para contar
//float grados; //Variable para almacenar el valor evaluado
//float preciso; //Variable para o mejorar la precison de valor medido
// 
//// Asignacion de una identificacion a la brujula
//Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);
// 
//void displaySensorDetails(void)
//{
//sensor_t sensor;
//mag.getSensor(&sensor);
//Serial.println("------------------------------------");
//Serial.print ("Sensor: "); Serial.println(sensor.name);
//Serial.print ("Driver Ver: "); Serial.println(sensor.version);
//Serial.print ("ID unica: "); Serial.println(sensor.sensor_id);
//Serial.print ("Valor Maximo: "); Serial.print(sensor.max_value); Serial.println(" uT");
//Serial.print ("Valor Minimo: "); Serial.print(sensor.min_value); Serial.println(" uT");
//Serial.print ("Resolucion: "); Serial.print(sensor.resolution); Serial.println(" uT");
//Serial.println("------------------------------------");
//Serial.println("");
//delay(500);
// 
//}
// 
//void setup(void)
//{
//Serial.begin(9600);
//Serial.println("Magnetometro HMC5883 Test"); Serial.println("");
// 
///* Inicializamos el sensor */
//if(!mag.begin()){
//// Si hay algun problema con el HMC5883 sale el aviso de que revise las conexiones
//Serial.println("Ooops, no se ha detectado el HMC5883 ... revisa las conexiones!");
//while(1);
//}
//Wire.begin(); //Inicia la comunicacion I2C
// 
////Configura a brújula
//brujula = HMC5883L();
//brujula.SetScale(1.3);
//brujula.SetMeasurementMode(Measurement_Continuous);
////===================
// 
//// Muesta la información básica del sensor
//displaySensorDetails();
//}
// 
//void loop(void)
//{
//// Hacemos que el sensor tome una nueva muestra
//sensors_event_t event;
//mag.getEvent(&event);
// 
//float muestra = atan2(event.magnetic.y, event.magnetic.x);
//preciso = 0; //A cero, la variable para una nueva lectura
// 
///* Una vez tengamos la muestra tomada, a continuación debemos agregar el "Ángulo de declinación"
//el ángulo de declinación es el "error" del campo magnético en su ubicación.
//Puede encontrar el suyo aquí: http://www.magnetic-declination.com/
//Si no encuentra su ángulo de declinación, comente las dos líneas siguientes, la brújula estará
//ligeramente desviada*/
// 
//float declinacionAngulo = 0.13; // Valencia, angulo de declinación 0.13
//muestra += declinacionAngulo;
// 
//// corrige los valores negativos
//if(muestra < 0)
//muestra += 2*PI;
// 
//// Comprueba si hay error debido a la adición de la declinación.
//if(muestra > 2*PI)
//muestra -= 2*PI;
//
//}

