import rclpy
from rclpy.node import Node
from sensor_msgs.msg import JointState
import serial

class JointToSerialNode(Node):
    def __init__(self):
        super().__init__('joint_to_serial')
        
        # Suscripción al tópico 'joint_states'
        self.subscription = self.create_subscription(
            JointState,
            'joint_states',
            self.listener_callback,
            10)
        
        # Configurar conexión serial con el Arduino
        self.arduino = serial.Serial('/dev/ttyACM0', 115200, timeout=1)  # Cambia el puerto si es necesario

        # Almacenar los últimos valores enviados
        self.last_angles = []

    def listener_callback(self, msg):
        # Convertir de radianes (-1.57 a 1.57) a grados (0 a 180)
        angles_in_degrees = [
            int((angle + 1.57) * (180.0 / 3.14159)) for angle in msg.position
        ]
        
        # Limitar la lista a los primeros 5 valores si hay más
        angles_in_degrees = angles_in_degrees[:5]
        
        # Imprimir los valores recibidos para ver los ángulos en grados
        self.get_logger().info(f"Valores recibidos: {angles_in_degrees}")
        
        # Verificar si ha habido un cambio en los valores
        if angles_in_degrees != self.last_angles:
            # Crear la cadena de ángulos
            angles_string = "/".join(map(str, angles_in_degrees))
            
            # Enviar la cadena por el puerto serial al Arduino
            self.arduino.write(f"{angles_string}\n".encode('utf-8'))
            print(f"{angles_string}\n")
            self.get_logger().info(f"Ángulos enviados: {angles_string}")
            
            # Actualizar los últimos ángulos enviados
            self.last_angles = angles_in_degrees

def main(args=None):
    rclpy.init(args=args)
    joint_to_serial_node = JointToSerialNode()
    rclpy.spin(joint_to_serial_node)
    joint_to_serial_node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
