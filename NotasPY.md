# Python en ROS 2 - Guia de Referencia

Guia de referencia para desarrollar nodos en ROS 2 con Python usando la biblioteca `rclpy`.

### [`↩️ Volver al inicio`](./README.md)

---

## API de ROS 2 con rclpy

| Metodo    | Tema | Descripcion | Ejemplo de Uso  |
|-----------|------|-------------|-----------------|
| **Nodos** |      |             |                 |
| `rclpy.init()`                    | Nodo      | Inicializa la biblioteca rclpy.                             | `rclpy.init()`                              |
| `Node()`                          | Nodo      | Crea un nodo en el sistema ROS 2.                           | `node = rclpy.create_node('nombre_del_nodo')` |
| `get_logger()`                    | Nodo      | Obtiene el objeto logger para imprimir mensajes de registro. | `logger = node.get_logger()`<br>`logger.info('Mensaje de informacion')` |
| `spin()`                          | Nodo      | Mantiene el nodo en ejecucion, procesando callbacks.        | `rclpy.spin(node)`                          |
| `shutdown()`                      | Nodo      | Apaga la biblioteca rclpy y destruye el nodo.              | `rclpy.shutdown()`                          |
| **Topicos** |      |             |                 |
| `create_subscription()`           | Topico    | Crea un suscriptor para recibir mensajes de un topico.      | `subscription = node.create_subscription(`<br>`    std_msgs.msg.String, 'topic', callback_function)` |
| `create_publisher()`              | Topico    | Crea un publicador para enviar mensajes a un topico.        | `publisher = node.create_publisher(`<br>`    std_msgs.msg.String, 'topic', 10)` |
| `publish()`                       | Topico    | Publica un mensaje a un topico.                             | `msg = std_msgs.msg.String(data='Hola, ROS2')`<br>`publisher.publish(msg)` |
| `destroy_subscription()`          | Topico    | Destruye un suscriptor especifico.                           | `node.destroy_subscription(subscription)`   |
| `destroy_publisher()`             | Topico    | Destruye un publicador especifico.                           | `node.destroy_publisher(publisher)`         |
| **Servicios** |      |             |                 |
| `create_service()`                | Servicio  | Crea un servicio para manejar solicitudes y respuestas.      | `service = node.create_service(`<br>`    std_srvs.srv.SetBool, 'service_name', callback_function)` |
| `call_service()`                  | Servicio  | Llama a un servicio y espera su respuesta.                  | `client = node.create_client(`<br>`    std_srvs.srv.SetBool, 'service_name')`<br>`response = client.call_async(request)` |
| `destroy_service()`               | Servicio  | Destruye un servicio especifico.                             | `node.destroy_service(service)`             |
| **Acciones** |      |             |                 |
| `create_action_server()`          | Accion     | Crea un servidor de accion para gestionar acciones.          | `action_server = rclpy.action.ActionServer(node,`<br>`    MyAction, 'action_name', execute_callback)` |
| `create_action_client()`          | Accion     | Crea un cliente de accion para enviar metas a un servidor.   | `action_client = rclpy.action.ActionClient(node,`<br>`    MyAction, 'action_name')` |
| `send_goal()`                     | Accion     | Envia un objetivo al servidor de accion.                     | `goal_handle = action_client.send_goal_async(goal)` |
| `wait_for_result()`               | Accion     | Espera el resultado de una accion despues de enviar un objetivo. | `result_future = action_client.wait_for_result(goal_handle)` |
| `get_result()`                    | Accion     | Obtiene el resultado de la accion completada.               | `result = result_future.result()`           |
| `destroy_action_server()`         | Accion     | Destruye un servidor de accion especifico.                  | `action_server.destroy()`                    |
| `destroy_action_client()`         | Accion     | Destruye un cliente de accion especifico.                   | `action_client.destroy()`                    |

---

## POO con Python

| Concepto                          | Descripcion                                                          | Ejemplo de Uso                                                 |
|-----------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------|
| **Definicion de Clase**           | Define una nueva clase en Python.                                   | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`pass`                                |
| **Constructor**                   | Metodo especial que se llama al crear una instancia de la clase.   | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self, valor):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self.valor = valor` |
| **Metodo**                        | Funcion definida dentro de una clase que opera en instancias.      | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def mi_metodo(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return self.valor` |
| **Herencia**                      | Permite que una clase herede atributos y metodos de otra clase.    | `class ClaseBase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`pass`<br>`class ClaseDerivada(ClaseBase):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`pass` |
| **Sobrecarga de Metodos**        | Permite definir metodos con el mismo nombre pero diferentes parametros (no soportado directamente en Python). | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def metodo(self, a):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return a`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def metodo(self, a, b):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return a + b` |
| **Polimorfismo**                 | Permite que un mismo metodo tenga diferentes implementaciones en diferentes clases. | `class Animal:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def hacer_sonido(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`pass`<br>`class Perro(Animal):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def hacer_sonido(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return "Guau"`<br>`class Gato(Animal):`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def hacer_sonido(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return "Miau"` |
| **Encapsulamiento**               | Restringe el acceso a ciertos atributos o metodos dentro de la clase. | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self.__valor_privado = 10`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def obtener_valor(self):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return self.__valor_privado` |
| **Atributos de Clase**           | Atributos que pertenecen a la clase en lugar de a instancias individuales. | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`atributo_clase = 0`                |
| **Atributos de Instancia**       | Atributos que pertenecen a una instancia especifica de la clase.   | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def __init__(self, valor):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`self.valor_instancia = valor` |
| **Metodo Estatico**              | Metodo que pertenece a la clase y no requiere acceso a la instancia. | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`@staticmethod`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def metodo_estatico():`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return "Hola"` |
| **Metodo de Clase**              | Metodo que recibe la clase como primer argumento en lugar de la instancia. | `class MiClase:`<br>&nbsp;&nbsp;&nbsp;&nbsp;`@classmethod`<br>&nbsp;&nbsp;&nbsp;&nbsp;`def metodo_clase(cls):`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`return cls` |

---

### [`↩️ Volver al inicio`](./README.md)
