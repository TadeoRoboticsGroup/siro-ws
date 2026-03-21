# C++ en ROS 2 - Guia de Referencia

Guia de referencia para desarrollar nodos en ROS 2 con C++ usando la biblioteca `rclcpp`.

### [`↩️ Volver al inicio`](./README.md)

---

### ESPACIO DE TRABAJO

1. **Crear un Workspace**

Crea un nuevo workspace para tu proyecto:
```bash
mkdir -p ~/siro_ws/src
cd ~/siro_ws/src
```

2. **Instalar Turtlesim**

Si no tienes el paquete turtlesim, instalalo:
```bash
sudo apt update
sudo apt install ros-humble-desktop
```

3. **Compilar el Workspace**

Regresa al directorio del workspace y compila:

```bash
cd ~/siro_ws
colcon build
source install/setup.bash

```

4. **Iniciar Turtlesim**

Abre un nuevo terminal y ejecuta el nodo de turtlesim:

```bash
ros2 run turtlesim turtlesim_node
```

### SERVICIOS 

5. Crear un Nodo Personalizado

Crea un nuevo paquete en tu workspace:


```bash
cd ~/siro_ws/src
ros2 pkg create --build-type ament_cmake my_turtle_controller
```

6. **Crear el Código para el Nodo**

Navega al directorio del nuevo paquete:

```bash
cd src/my_turtle_controller
```
Crea el archivo `turtle_controller.cpp` en la carpeta `src`:

```cpp
#include <rclcpp/rclcpp.hpp>
#include <geometry_msgs/msg/twist.hpp>

class TurtleController : public rclcpp::Node {
public:
    TurtleController() : Node("turtle_controller") {
        publisher_ = this->create_publisher<geometry_msgs::msg::Twist>("turtle1/cmd_vel", 10);
        timer_ = this->create_wall_timer(
            std::chrono::milliseconds(500),
            std::bind(&TurtleController::timer_callback, this));
    }

private:
    void timer_callback() {
        auto message = geometry_msgs::msg::Twist();
        message.linear.x = 2.0;  // Velocidad lineal
        message.angular.z = 1.0;  // Velocidad angular
        publisher_->publish(message);
        RCLCPP_INFO(this->get_logger(), "Publicando: x: '%f', z: '%f'", message.linear.x, message.angular.z);
    }

    rclcpp::Publisher<geometry_msgs::msg::Twist>::SharedPtr publisher_;
    rclcpp::TimerBase::SharedPtr timer_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TurtleController>());
    rclcpp::shutdown();
    return 0;
}

```

7. **Modificar el CMakeLists.txt**

Edita el archivo `CMakeLists.txt` para incluir las dependencias necesarias:

```cmake
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)

add_executable(turtle_controller src/turtle_controller.cpp)
ament_target_dependencies(turtle_controller rclcpp geometry_msgs)

install(TARGETS
  turtle_controller
  DESTINATION lib/${PROJECT_NAME})

```

8. **Compilar el Nodo**

Compila el nuevo nodo:

```bash
cd ~/siro_ws
colcon build
source install/setup.bash
```

9. **Ejecutar el Nodo**

Ahora, ejecuta tu nodo de control:

```bash
ros2 run my_turtle_controller turtle_controller
```

Deberías ver que la tortuga en `turtlesim` se mueve automáticamente.

10. **Crear un Servicio**

Para agregar un servicio, crea un nuevo archivo en src llamado turtle_service.cpp:

```cpp
#include <rclcpp/rclcpp.hpp>
#include <std_srvs/srv/empty.hpp>

class TurtleService : public rclcpp::Node {
public:
    TurtleService() : Node("turtle_service") {
        service_ = this->create_service<std_srvs::srv::Empty>(
            "reset_turtle",
            std::bind(&TurtleService::reset_callback, this, std::placeholders::_1, std::placeholders::_2));
    }

private:
    void reset_callback(const std::shared_ptr<rmw_request_id_t> request_header,
                        const std::shared_ptr<std_srvs::srv::Empty::Request> request,
                        const std::shared_ptr<std_srvs::srv::Empty::Response> response) {
        RCLCPP_INFO(this->get_logger(), "Resetting the turtle");
        // Aquí podrías enviar un comando para reiniciar la tortuga
    }

    rclcpp::Service<std_srvs::srv::Empty>::SharedPtr service_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<TurtleService>());
    rclcpp::shutdown();
    return 0;
}
```

11. **Modificar CMakeLists.txt para el Servicio**

Asegúrate de agregar la dependencia del servicio en tu `CMakeLists.txt`:

```cmake
find_package(std_srvs REQUIRED)

add_executable(turtle_service src/turtle_service.cpp)
ament_target_dependencies(turtle_service rclcpp std_srvs)

install(TARGETS
  turtle_service
  DESTINATION lib/${PROJECT_NAME})

```
12. **Compilar y Ejecutar el Servicio**

Vuelve a compilar el proyecto:

```bash
cd ~/siro_ws
colcon build
source install/setup.bash
```
Ejecuta el servicio:
```bash
ros2 run my_turtle_controller turtle_service
```

Para llamar al servicio, puedes abrir otro terminal y usar:
```bash
rros2 service call /reset_turtle std_srvs/srv/Empty
```
### ACCIONES

13. **Crear un Paquete para la Acción**

Primero, crea un nuevo paquete donde definiremos la acción. Navega a tu workspace y crea un paquete nuevo:

```bash
cd ~/siro_ws/src
ros2 pkg create --build-type ament_cmake my_turtle_actions
```
14. **Crear la Definición de Acción**

Crea una carpeta llamada `action` dentro del nuevo paquete:

```bash
cd my_turtle_actions
mkdir action
```
Dentro de la carpeta action, crea un archivo llamado MoveTurtle.action:

```bash
# Goal
float64 distance

---
# Result
float64 final_position

---
# Feedback
float64 current_position

```

15. **Modificar CMakeLists.txt**

Asegúrate de que tu `CMakeLists.txt` esté configurado para generar el código de la acción. Añade lo siguiente:

```cmake
find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "action/MoveTurtle.action"
)
```

Y no olvides agregar las dependencias necesarias:

```cmake
find_package(rclcpp REQUIRED)
find_package(action_msgs REQUIRED)
```

16. **Crear el Nodo de Acción**

Ahora, crea un archivo llamado `move_turtle_action_server.cpp` en la carpeta `src`:

```cpp
#include <rclcpp/rclcpp.hpp>
#include <action_msgs/msg/goal_info.hpp>
#include <rclcpp_action/rclcpp_action.hpp>
#include "my_turtle_actions/action/move_turtle.hpp"

class MoveTurtleAction : public rclcpp::Node {
public:
    using MoveTurtle = my_turtle_actions::action::MoveTurtle;
    using GoalHandleMoveTurtle = rclcpp_action::ServerGoalHandle<MoveTurtle>;

    MoveTurtleAction() : Node("move_turtle_action") {
        this->action_server_ = rclcpp_action::create_server<MoveTurtle>(
            this->get_node_base_interface(),
            this->get_node_clock_interface(),
            this->get_node_logging_interface(),
            this->get_node_parameters_interface(),
            "move_turtle",
            std::bind(&MoveTurtleAction::handle_goal, this, std::placeholders::_1, std::placeholders::_2),
            std::bind(&MoveTurtleAction::handle_cancel, this, std::placeholders::_1),
            std::bind(&MoveTurtleAction::handle_accepted, this, std::placeholders::_1));
    }

private:
    rclcpp_action::Server<MoveTurtle>::SharedPtr action_server_;

    rclcpp_action::GoalResponse handle_goal(
        const rclcpp_action::GoalUUID & uuid,
        std::shared_ptr<const MoveTurtle::Goal> goal) {
        RCLCPP_INFO(this->get_logger(), "Recibido objetivo: %f", goal->distance);
        return rclcpp_action::GoalResponse::Accepted;
    }

    rclcpp_action::CancelResponse handle_cancel(const std::shared_ptr<GoalHandleMoveTurtle> goal_handle) {
        RCLCPP_INFO(this->get_logger(), "Cancelando objetivo");
        return rclcpp_action::CancelResponse::Accepted;
    }

    void handle_accepted(const std::shared_ptr<GoalHandleMoveTurtle> goal_handle) {
        std::thread{
            [this, goal_handle]() {
                const auto goal = goal_handle->get_goal();
                auto feedback = std::make_shared<MoveTurtle::Feedback>();
                auto result = std::make_shared<MoveTurtle::Result>();

                // Simulación de movimiento
                for (double i = 0; i < goal->distance; i += 0.1) {
                    feedback->current_position = i;
                    goal_handle->publish_feedback(feedback);
                    std::this_thread::sleep_for(std::chrono::milliseconds(100));
                }
                result->final_position = goal->distance;
                goal_handle->succeed(result);
            }
        }.detach();
    }
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    rclcpp::spin(std::make_shared<MoveTurtleAction>());
    rclcpp::shutdown();
    return 0;
}

```
17. **Modificar CMakeLists.txt para el Nodo de Acción**

Asegúrate de que tu C`MakeLists.txt` incluya el nuevo archivo fuente:

```cmake
add_executable(move_turtle_action_server src/move_turtle_action_server.cpp)
ament_target_dependencies(move_turtle_action_server rclcpp rclcpp_action my_turtle_actions)

install(TARGETS
  move_turtle_action_server
  DESTINATION lib/${PROJECT_NAME})

```
18. **Compilar y Ejecutar el Servidor de Acción**

Ahora compila el proyecto:

```bash
cd ~/siro_ws
colcon build
source install/setup.bash
```

Ejecuta el servidor de acción:

```bash
ros2 run my_turtle_actions move_turtle_action_server
```

19. **Crear un Cliente de Acción**
Para probar el servidor de acción, crea un nuevo archivo en `src` llamado `move_turtle_action_client.cpp`:

```cpp
#include <rclcpp/rclcpp.hpp>
#include <rclcpp_action/rclcpp_action.hpp>
#include "my_turtle_actions/action/move_turtle.hpp"

class MoveTurtleClient : public rclcpp::Node {
public:
    using MoveTurtle = my_turtle_actions::action::MoveTurtle;
    using GoalHandleMoveTurtle = rclcpp_action::ClientGoalHandle<MoveTurtle>;

    MoveTurtleClient() : Node("move_turtle_client") {
        client_ = rclcpp_action::create_client<MoveTurtle>(this, "move_turtle");
    }

    void send_goal(double distance) {
        if (!client_->wait_for_action_server(std::chrono::seconds(10))) {
            RCLCPP_ERROR(this->get_logger(), "No se pudo conectar al servidor de acción");
            return;
        }

        auto goal_msg = MoveTurtle::Goal();
        goal_msg.distance = distance;

        RCLCPP_INFO(this->get_logger(), "Enviando objetivo: %f", goal_msg.distance);

        auto send_goal_options = rclcpp_action::Client<MoveTurtle>::SendGoalOptions();
        send_goal_options.result_callback = std::bind(&MoveTurtleClient::result_callback, this, std::placeholders::_1);
        send_goal_options.feedback_callback = std::bind(&MoveTurtleClient::feedback_callback, this, std::placeholders::_1, std::placeholders::_2);

        client_->async_send_goal(goal_msg, send_goal_options);
    }

private:
    void result_callback(const GoalHandleMoveTurtle::WrappedResult & result) {
        switch (result.code) {
            case rclcpp_action::ResultCode::SUCCEEDED:
                RCLCPP_INFO(this->get_logger(), "Acción completada con éxito");
                break;
            default:
                RCLCPP_ERROR(this->get_logger(), "La acción falló");
                break;
        }
    }

    void feedback_callback(GoalHandleMoveTurtle::SharedPtr, const std::shared_ptr<const MoveTurtle::Feedback> feedback) {
        RCLCPP_INFO(this->get_logger(), "Posición actual: %f", feedback->current_position);
    }

    rclcpp_action::Client<MoveTurtle>::SharedPtr client_;
};

int main(int argc, char **argv) {
    rclcpp::init(argc, argv);
    auto client = std::make_shared<MoveTurtleClient>();
    client->send_goal(1.0); // Envía un objetivo de distancia de 1.0
    rclcpp::spin(client);
    rclcpp::shutdown();
    return 0;
}
```

20. **Modificar CMakeLists.txt para el Cliente de Acción**

Agrega el nuevo archivo fuente en tu CMakeLists.txt:

```cpp
add_executable(move_turtle_action_client src/move_turtle_action_client.cpp)
ament_target_dependencies(move_turtle_action_client rclcpp rclcpp_action my_turtle_actions)

install(TARGETS
  move_turtle_action_client
  DESTINATION lib/${PROJECT_NAME})
```

21. **Compilar y Ejecutar el Cliente de Acción**

Compila el proyecto nuevamente:

```bash
cd ~/siro_ws
colcon build
source install/setup.bash
```

Ejecuta el cliente de acción en un terminal separado:

```bash
ros2 run my_turtle_actions move_turtle_action_client
```

---

## API de ROS 2 con rclcpp

| Metodo                                | Tema      | Descripcion                                                  | Ejemplo de Uso                                                 |
|---------------------------------------|-----------|--------------------------------------------------------------|---------------------------------------------------------------|
| **Nodos**                             |           |                                                              |                                                               |
| `rclcpp::init()`                     | Nodo      | Inicializa la biblioteca rclcpp.                            | `rclcpp::init(argc, argv);`                   |
| `std::make_shared<Node>()`           | Nodo      | Crea un nodo en el sistema ROS 2.                           | `auto node = std::make_shared<rclcpp::Node>("nombre_del_nodo");` |
| `get_logger()`                        | Nodo      | Obtiene el objeto logger para imprimir mensajes de registro. | `RCLCPP_INFO(node->get_logger(), "Mensaje de informacion");` |
| `spin()`                              | Nodo      | Mantiene el nodo en ejecucion, procesando callbacks.        | `rclcpp::spin(node);`                         |
| `shutdown()`                          | Nodo      | Apaga la biblioteca rclcpp y destruye el nodo.             | `rclcpp::shutdown();`                          |
| **Topicos**                           |           |                                                              |                                                               |
| `create_subscription()`               | Topico    | Crea un suscriptor para recibir mensajes de un topico.      | `auto subscription = node->create_subscription<std_msgs::msg::String>(`<br>`    "topic", callback_function);` |
| `create_publisher()`                  | Topico    | Crea un publicador para enviar mensajes a un topico.        | `auto publisher = node->create_publisher<std_msgs::msg::String>("topic", 10);` |
| `publish()`                           | Topico    | Publica un mensaje a un topico.                             | `std_msgs::msg::String msg;`<br>`msg.data = "Hola, ROS2";`<br>`publisher->publish(msg);` |
| `destroy_subscription()`              | Topico    | Destruye un suscriptor especifico.                           | `node->destroy_subscription(subscription);`   |
| `destroy_publisher()`                 | Topico    | Destruye un publicador especifico.                           | `node->destroy_publisher(publisher);`         |
| **Servicios**                         |           |                                                              |                                                               |
| `create_service()`                    | Servicio  | Crea un servicio para manejar solicitudes y respuestas.      | `auto service = node->create_service<std_srvs::srv::SetBool>(`<br>`    "service_name", callback_function);` |
| `create_client()`                     | Servicio  | Crea un cliente para llamar a un servicio.                  | `auto client = node->create_client<std_srvs::srv::SetBool>("service_name");` |
| `call_service()`                      | Servicio  | Llama a un servicio y espera su respuesta.                  | `auto future = client->async_send_request(request);` |
| `destroy_service()`                   | Servicio  | Destruye un servicio especifico.                             | `node->destroy_service(service);`             |
| **Acciones**                          |           |                                                              |                                                               |
| `create_action_server()`              | Accion     | Crea un servidor de accion para gestionar acciones.          | `auto action_server = rclcpp_action::create_server<MyAction>(`<br>`    node,`<br>`    "action_name", execute_callback);` |
| `create_action_client()`              | Accion     | Crea un cliente de accion para enviar metas a un servidor.   | `auto action_client = rclcpp_action::create_client<MyAction>(node, "action_name");` |
| `send_goal()`                         | Accion     | Envia un objetivo al servidor de accion.                     | `auto future = action_client->async_send_goal(goal);` |
| `wait_for_result()`                   | Accion     | Espera el resultado de una accion despues de enviar un objetivo. | `auto result_future = action_client->async_get_result(goal_handle);` |
| `get_result()`                        | Accion     | Obtiene el resultado de la accion completada.               | `auto result = result_future.get();`          |
| `destroy_action_server()`             | Accion     | Destruye un servidor de accion especifico.                  | `action_server->destroy();`                   |
| `destroy_action_client()`             | Accion     | Destruye un cliente de accion especifico.                   | `action_client->destroy();`                   |

---

## POO con C++

| Concepto                          | Descripcion                                                          | Ejemplo de Uso                                                 |
|-----------------------------------|----------------------------------------------------------------------|---------------------------------------------------------------|
| **Definicion de Clase**           | Define una nueva clase en C++.                                      | `class MiClase {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`public:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`MiClase();`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`~MiClase();`<br>&nbsp;&nbsp;&nbsp;&nbsp;`};` |
| **Constructor**                   | Metodo especial que se llama al crear una instancia de la clase.    | `MiClase::MiClase() { /* Constructor */ }`                   |
| **Destructor**                    | Metodo especial que se llama al destruir una instancia de la clase. | `MiClase::~MiClase() { /* Destructor */ }`                    |
| **Metodo**                        | Funcion definida dentro de una clase que opera en instancias.       | `void MiClase::miMetodo() { /* codigo */ }`                  |
| **Herencia**                      | Permite que una clase herede atributos y metodos de otra clase.     | `class ClaseBase { };`<br>`class ClaseDerivada : public ClaseBase { };` |
| **Sobrecarga de Metodos**        | Permite definir metodos con el mismo nombre pero diferentes parametros. | `void metodo(int a) { /* codigo */ }`<br>`void metodo(double b) { /* codigo */ }` |
| **Polimorfismo**                 | Permite que un mismo metodo tenga diferentes implementaciones en diferentes clases. | `class Animal { public: virtual void hacerSonido(); };`<br>`class Perro : public Animal { public: void hacerSonido() override; };` |
| **Encapsulamiento**               | Restringe el acceso a ciertos atributos o metodos dentro de la clase. | `class MiClase {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`private:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`int valorPrivado;`<br>&nbsp;&nbsp;&nbsp;&nbsp;`public:`<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`int getValorPrivado() { return valorPrivado; }`<br>`};` |
| **Atributos de Clase**           | Atributos que pertenecen a la clase en lugar de a instancias individuales. | `class MiClase {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`static int atributoClase;`<br>`};` |
| **Atributos de Instancia**       | Atributos que pertenecen a una instancia especifica de la clase.    | `class MiClase {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`int valorInstancia;`<br>`};` |
| **Metodo Estatico**              | Metodo que pertenece a la clase y no requiere acceso a la instancia. | `class MiClase {`<br>&nbsp;&nbsp;&nbsp;&nbsp;`static void metodoEstatico() { /* codigo */ }`<br>`};` |

---

### [`↩️ Volver al inicio`](./README.md)