#include <Servo.h>

Servo baseServo;
Servo shoulderServo;
Servo elbowServo;
Servo wristServo;
Servo gripperServo;

void setup() {
  // Configurar los pines de los servos
  baseServo.attach(4);
  shoulderServo.attach(6);
  elbowServo.attach(8);
  wristServo.attach(11);
  gripperServo.attach(15);
  
  // Iniciar la comunicación serial
  Serial.begin(115200);
}

void loop() {
  if (Serial.available() > 0) {
    // Leer la cadena de ángulos enviada desde el nodo de ROS2
    String anglesString = Serial.readStringUntil('\n');
    Serial.println("Valores recibidos: " + anglesString); // Imprimir para ver los valores

    // Dividir la cadena en ángulos individuales
    int angles[5];
    int index = 0;
    int startPos = 0;

    for (int i = 0; i < anglesString.length(); i++) {
      if (anglesString[i] == '/') {
        angles[index++] = anglesString.substring(startPos, i).toInt();
        startPos = i + 1;
      }
    }
    angles[index] = anglesString.substring(startPos).toInt();

    // Asignar cada ángulo al servo correspondiente
    baseServo.write(angles[0]);
    shoulderServo.write(angles[1]);
    elbowServo.write(angles[2]);
    wristServo.write(angles[3]);
    gripperServo.write(angles[4]);
  }
}
