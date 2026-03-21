# SIRO ARM - Brazo Robotico con ROS 2

Proyecto de un brazo robotico controlado desde ROS 2 con comunicacion serial a Arduino.

### [`↩️ Volver al inicio`](./README.md)

---

## Arquitectura del sistema

```
ROS 2 (PC)                          Arduino
┌─────────────────────┐              ┌──────────────┐
│  joint_state_pub_gui│──/joint_──>  │              │
│  (deslizadores)     │   states     │  5 Servos    │
│                     │              │  (pines 9-13)│
│  robot_state_pub    │   Serial     │              │
│  (URDF -> TF)       │──USB────────>│              │
│                     │   9600 baud  │              │
│  rviz2             │              │              │
│  (visualizacion)    │              │              │
│                     │              │              │
│  serial_publisher   │              │              │
│  (nodo puente)      │              │              │
└─────────────────────┘              └──────────────┘
```

---

## Launch file

Lanza `robot_state_publisher`, `rviz2` y el nodo de comunicacion serial:

```python
def generate_launch_description():
    urdf_file = os.path.join(
        get_package_share_directory('siro_arm'), 'urdf', 'arm1.urdf'
    )

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'robot_description': open(urdf_file).read()}]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            arguments=['-d', os.path.join(
                get_package_share_directory('siro_arm'), 'config', 'siro_arm.rviz'
            )],
        ),
        Node(
            package='siro_arm',
            executable='serial_publisher',
            name='serial_publisher',
            output='screen',
        )
    ])
```

---

## Nodo serial_publisher

Suscribe a `/joint_states` y envia las posiciones de los joints por serial al Arduino:

```python
import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial

class SerialPublisher(Node):
    def __init__(self):
        super().__init__('serial_publisher')
        self.subscription = self.create_subscription(
            JointState,
            '/joint_states',
            self.joint_states_callback,
            10
        )
        self.serial_connection = serial.Serial('/dev/ttyUSB0', 9600)

    def joint_states_callback(self, msg):
        positions = msg.position
        command = ','.join(map(str, positions)) + '\n'
        self.serial_connection.write(command.encode())

def main(args=None):
    rclpy.init(args=args)
    serial_publisher = SerialPublisher()
    rclpy.spin(serial_publisher)
    serial_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

> **Nota**: Ajustar el puerto serial (`/dev/ttyUSB0`) y velocidad (`9600`) segun la configuracion del Arduino.

---

## Codigo Arduino

Recibe las posiciones por serial y mueve 5 servomotores:

```c
#include <Servo.h>

Servo servo1, servo2, servo3, servo4, servo5;
int pos1, pos2, pos3, pos4, pos5;

void setup() {
    Serial.begin(9600);
    servo1.attach(9);
    servo2.attach(10);
    servo3.attach(11);
    servo4.attach(12);
    servo5.attach(13);
}

void loop() {
    if (Serial.available() > 0) {
        String data = Serial.readStringUntil('\n');

        int c1 = data.indexOf(',');
        int c2 = data.indexOf(',', c1 + 1);
        int c3 = data.indexOf(',', c2 + 1);
        int c4 = data.indexOf(',', c3 + 1);

        pos1 = data.substring(0, c1).toInt();
        pos2 = data.substring(c1 + 1, c2).toInt();
        pos3 = data.substring(c2 + 1, c3).toInt();
        pos4 = data.substring(c3 + 1, c4).toInt();
        pos5 = data.substring(c4 + 1).toInt();

        servo1.write(pos1);
        servo2.write(pos2);
        servo3.write(pos3);
        servo4.write(pos4);
        servo5.write(pos5);
    }
}
```

---

## Dependencias

```bash
# ROS 2
sudo apt install ros-humble-joint-state-publisher-gui
sudo apt install ros-humble-robot-state-publisher

# Python
pip install pyserial
```

---

### [`↩️ Volver al inicio`](./README.md)
