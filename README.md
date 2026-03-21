# 🎯APRENDIENDO  SOBRE ROS 🤖🚀🕹️

<div id="header" align="center">
    <img src="/images/ros-image2.png" alt="ros humble" width="50%" max-width="100%">
</div>


**ROS2** (*Robot Operating System 2*) es una plataforma de código abierto diseñada para facilitar el desarrollo, operación y mantenimiento de sistemas robóticos y de automatización industrial. Ofrece una arquitectura modular y flexible que permite la comunicación entre componentes distribuidos, soportando una variedad de sistemas operativos y arquitecturas de hardware. ROS 2 se destaca por su capacidad de escalabilidad, seguridad y robustez, lo que lo convierte en una herramienta crucial para la creación de sistemas robóticos avanzados en diversos entornos industriales y de investigación.

## Tabla de contenidos

| # | Tema | Descripción |
|---|------|-------------|
| 1 | [Historia](#historia) | Origen de ROS y evolución a ROS 2 |
| 2 | [Diferencias ROS1 vs ROS2](#diferencias-entre-ros1-y-ros2) | Arquitectura centralizada vs distribuida |
| 3 | [Arquitectura ROS2](#arquitectura-ros2) | DDS, nodos, middleware y comunicación |
| 4 | [Nodos](#nodos) | Bloques de código independientes del robot |
| 5 | [Tópicos](#topicos) | Comunicación asíncrona (Pub/Sub) |
| 6 | [Servicios](#servicios) | Comunicación síncrona (Request/Response) |
| 7 | [Acciones](#acciones) | Tareas largas con feedback (Goal/Result/Feedback) |
| 8 | [Interfaces](#interfaces) | Definición de mensajes, servicios y acciones |
| 9 | [Parámetros](#parametros) | Configuración dinámica de nodos |
| 10 | [Launch](#launch) | Lanzar múltiples nodos con un solo comando |
| 11 | [Virtualización (URDF)](#virtualización-de-un-robot) | Descripción del robot con links y joints |

> Todos los ejemplos usan el paquete **turtlesim**. Para instalarlo ve a la [guía de instalación](./INSTALL.md).

## Historia

**ROS** en su primera versión, **ROS1**, se desarrolló en los Laboratorios de Inteligencia Artificial de Stanford (SAIL) por estudiantes de doctorado **Eric Berger** y **Keenan Wyrobek**. Se publicó bajo una **licencia BSD** de software libre en 2007, que permite libertad para uso comercial e investigador. Desde 2008, el instituto **Willow Garage** se ha encargado principalmente del desarrollo y soporte.

La idea de crear un sistema operativo era estandarizar tareas como la *abstracción de hardware*, *control de dispositivos* de bajo nivel (drivers), implementación de *procesos comunes*, manejo de *comunicación*, *soporte* de paquetes y otras ventajas.

**ROS2** es la evolución natural del exitoso marco de trabajo **ROS1**. Desarrollado para abordar las limitaciones de su predecesor, ROS2 ofrece una *arquitectura modular* y *distribuida*, mejor *rendimiento* y *escalabilidad*, así como soporte *multiplataforma*. Lanzado oficialmente en 2015, ROS2 mantiene la *flexibilidad* y *robustez* de ROS1, al tiempo que introduce mejoras significativas en herramientas de desarrollo y comunicación. Su diseño modular permite una fácil integración con otros sistemas y una adaptación más rápida a diferentes entornos de desarrollo. Con características como compatibilidad con múltiples lenguajes de programación y una creciente comunidad de desarrolladores, ROS2 es la elección preferida para proyectos de robótica modernos y ambiciosos.

## Filosofía
***"ROS, nacido del corazón del código abierto, ofrece libertad y flexibilidad para que los usuarios moldeen su propia realidad robótica, trazando un camino lleno de posibilidades infinitas en el vasto horizonte de la tecnología"***.


## DIFERENCIAS ENTRE ROS1 Y ROS2

<div align="center">
    <img src="/images/ros1_vs_ros2_diagram.svg" alt="ROS1 vs ROS2" width="85%" max-width="100%">
</div>

| Característica        | ROS1          | ROS2        |
|-----------------------|---------------|-------------|
| **Arquitectura**  | Basada en un sistema de nodos con comunicación XML-RPC y TCP/IP | Arquitectura modular y distribuida, comunicación basada en DDS    |
| **Lenguajes de Programación** | Soporte para C++, Python, Lisp, entre otros                   | Soporte para varios lenguajes, incluyendo C++, Python, y más      |
| **Rendimiento** | Limitaciones en rendimiento, seguridad y escalabilidad         | Mejoras significativas en rendimiento, seguridad y escalabilidad  |
| **Multiplataforma** | Principalmente enfocado en Linux                               | Soporte multiplataforma incluyendo Linux, Windows, y macOS        |
| **Herramientas**  | Herramientas de desarrollo y depuración limitadas              | Mejoras en herramientas de depuración, simulación, y gestión de paquetes |
| **Compatibilidad**  | No es directamente compatible con ROS 2                        | Introduce puentes y herramientas de migración para la compatibilidad con ROS 1 |
| **Ecosistema**  | Ecosistema consolidado con una amplia comunidad                 | Ecosistema en constante crecimiento con una creciente comunidad de desarrolladores |




## Arquitectura ROS2
La arquitectura de ROS2 se ha diseñado para abordar las limitaciones de ROS1 y proporcionar una plataforma más flexible, escalable y robusta para el desarrollo de aplicaciones robóticas. A continuación, se proporciona una explicación paso a paso de la arquitectura de ROS2:

| Paso  | Descripción  |
|-------|----------------|
| 1. Arquitectura Modular y Distribuida | ROS 2 se basa en una arquitectura modular y distribuida, donde los nodos son componentes independientes que pueden ejecutarse de manera separada.          |
| 2. Comunicación Basada en DDS | Utiliza DDS para la comunicación entre nodos, ofreciendo un rendimiento superior, mayor seguridad y mejor escalabilidad que el sistema de ROS 1.            |
| 3. Nodos                     | Cada nodo en ROS 2 es un proceso independiente que realiza una tarea específica y se comunica con otros nodos intercambiando mensajes a través de DDS.     |
| 4. Middleware (DDS)          | DDS actúa como el middleware que facilita la comunicación entre nodos, proporcionando mecanismos eficientes para la publicación y suscripción de mensajes. |
| 5. Interfaces de Mensajería (IDL) | Utiliza interfaces de definición de lenguaje (IDL) para describir la estructura de los mensajes que se intercambian entre nodos.                        |
| 6. Gestión de Recursos       | Incluye una capa de gestión de recursos para asignar y administrar eficientemente los recursos del sistema, como memoria y procesamiento.                   |
| 7. Soporte Multiplataforma   | Diseñado para ser ejecutado en una variedad de sistemas operativos, incluyendo Linux, Windows y macOS, lo que proporciona mayor flexibilidad y portabilidad.  |


En resumen, la arquitectura de ROS2 se caracteriza por su modularidad, su sistema de comunicación basado en DDS, su soporte multiplataforma y su capacidad para gestionar eficientemente los recursos del sistema. Estas características hacen de ROS2 una plataforma poderosa y versátil para el desarrollo de aplicaciones robóticas modernas.

<br>
<div id="header" align="center">
    <img src="/images/arquitectura.png" alt="Arquitectura de ros" width="50%" max-width="100%">
</div>

### Formas de comunicación en ROS 2

<div id="header" align="center">
    <img src="/images/ros2_communication_overview.svg" alt="Comunicación en ROS 2" width="80%" max-width="100%">
</div>

<br>

## NODOS
Los nodos son bloques de código (clases) que se encargan de partes específicas de las actividades del robot. Estos se van a enlazar mediante tópicos, servicios o acciones. Básicamente nos ayudan a crear un sistema modular que se pueda modificar fácilmente y comunicar.

<div align="center">
    <img src="/images/nodes_diagram.svg" alt="Diagrama de Nodos" width="70%" max-width="100%">
</div>

### Comandos básicos
Usaremos el paquete turtlesim que puedes instalar [`aquí`](./turtlesim/README.md).

1. Ejecutar un nodo.
```bash
ros2 run turtlesim turtlesim_node
```
En este caso lanzamos el nodo que mediante rqt lanza una interfaz gráfica con una tortuga en unas coordenadas especificas.

<div id="header" align="center">
    <img src="/images/turtlesim_node.png" alt="turtlesim_node" width="50%" max-width="100%">
</div>

En una nueva consola ejecutamos un segundo nodo.
```bash
ros2 run turtlesim turtle_teleop_key
```
2. Para visualizar los nodos en ejecución:
```bash
ros2 node list
```
Lo cual nos mostrara que hay dos nodos en ejecución

```
/teleop_turtle
/turtlesim
```

3. Podemos cambiar los parámetros y argumentos en los nodos. Por ejemplo, cambiar el nombre del nodo `turtlesim` a `myturtle`, para ello vamos a abrir una nueva consola y ejecutar
```bash
ros2 run turtlesim turtlesim_node --ros-args --remap __node:=myturtle
```
Visualizamos nuevamente los nodos en ejecucón
```bash
ros2 node list
```
En este caso nos aparecen tres nodos en ejecución
```
/myturtle
/teleop_turtle
/turtlesim
```
4. **Información de un nodo**:  A veces se hace necesario conocer la información de un nodo para ver las suscripciones, qué está publicando, los servicios clientes, los servicios servidores y las acciones. Podemos ver la información de esta manera.
```bash
ros2 node info /turtlesim
```
En este caso vemos la información del nodo `/turtlesim`
```
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```

<br>

## TOPICOS
Son canales en los cuales unos nodos publican información y otros se suscriben para recibirla. La relación para la comunicación puede ser de  *muchos a uno*(one to many), *muchos a uno*(many to one) y *muchos a muchos*(many to many).

<div align="center">
    <img src="/images/topics_diagram.svg" alt="Diagrama de Tópicos" width="75%" max-width="100%">
</div>

### Características de los tópicos
- **Definición de Tópicos**:
Canales de comunicación identificados por un nombre único.
- **Tipos de Mensajes**:
Los mensajes transmitidos a través de los tópicos pueden ser de tipos estándar (std_msgs) o personalizados.
- **Publicación y Suscripción**:
Los nodos pueden publicar o suscribirse a un tópico para enviar o recibir mensajes.
- **Comunicación Desacoplada**:
La comunicación se realiza de forma asíncrona y desacoplada entre nodos.
- **Calidad de Servicio (QoS)**:
Configuraciones de QoS permiten ajustar la durabilidad, fiabilidad, latencia, entre otros aspectos de la comunicación.
- **Jerarquía de Nombres de los Tópicos**:
Los nombres de los tópicos pueden ser jerárquicos para organizar la información.
- **Tópicos Privados**:
Los nodos pueden usar tópicos privados para encapsular la comunicación dentro de un nodo o grupo de nodos.
- **Herramientas para Trabajar con Tópicos**:
Herramientas como `ros2 topic list` y `ros2 topic echo` permiten gestionar y monitorear los tópicos.


### Clasificación

En cuanto a los tipos de tópicos, no hay una clasificación específica de los tópicos en sí; más bien, los tópicos se definen por el tipo de mensajes que manejan y el propósito de los nodos que los utilizan.

1. **Tipos de mensajes estándar**:
ROS 2 proporciona una variedad de tipos de mensajes estándar definidos en varios paquetes como `std_msgs`, `geometry_msgs`, `sensor_msgs`, entre otros. Algunos ejemplos de mensajes estándar son:

  - **std_msgs**: Mensajes estándar.
    * **std_msgs/String**: Un mensaje de texto simple.
    * **std_msgs/Int32**: Un entero de 32 bits.
    * **std_msgs/Float32**: Un número de punto flotante de 32 bits.


  - **geometry_msgs**: Mensajes de geometría y movimiento.
    * **geometry_msgs/Point**
      - Representa un punto en un espacio tridimensional.
      - Contiene tres coordenadas: `x`, `y` y `z`.
      - *Ejemplo de uso*: Describir la posición de un objeto en un espacio 3D.
      ```
      geometry_msgs/Point {x: 1.0, y: 2.0, z: 3.0}
      ```
    
    * **geometry_msgs/Quaternion**
      - Representa una orientación en un espacio tridimensional utilizando un cuaternio.
      - Contiene cuatro componentes: `x`, `y`, `z`, y `w`.
      - *Ejemplo de uso*: Describir la orientación de un objeto en un espacio 3D.
      ```
      geometry_msgs/Quaternion {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
      ```

    * **geometry_msgs/Pose**
      - Representa la posición y la orientación de un objeto en un espacio tridimensional.
      - Combina `Point` y `Quaternion`.
      - *Ejemplo de uso*: Describir la pose de un robot o un objeto en un espacio 3D.
      ```
      geometry_msgs/Pose {position: {x: 1.0, y: 2.0, z: 3.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}
      ```

    * **geometry_msgs/Twist**
      - Representa el movimiento lineal y angular de un objeto.
      - *Contiene dos campos*: `linear` (un `Vector3` que describe la velocidad lineal) y `angular` (un `Vector3` que describe la velocidad angular).
      - *Ejemplo de uso*: Describir la velocidad de un robot o un objeto en un espacio 3D.
      ```
      geometry_msgs/Twist {linear: {x: 0.1, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.5}}
      ```

    * **geometry_msgs/PoseStamped**
      - Similar a `Pose`, pero incluye un sello de tiempo (`header.stamp`) y un marco de referencia (`header.frame_id`).
      - Combina `Point` y `Quaternion`.
      - Se utiliza para describir la pose de un objeto en un determinado momento y marco de referencia.
      ```
      geometry_msgs/PoseStamped { header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"}, pose: {position: {x: 1.0, y: 2.0, z: 3.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}
      ```
    
    * **geometry_msgs/Transform**
      - Representa una transformación que consiste en una rotación (`rotation`, un `Quaternion`) y una traslación (`translation`, un `Vector3`).
      - *Ejemplo de uso*: Describir cómo se transforma un objeto en relación con otro.
      ```
      geometry_msgs/Transform {translation: {x: 1.0, y: 2.0, z: 3.0}, rotation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}
      ```

    * **geometry_msgs/Wrench**
      - Representa fuerzas lineales y torques angulares que actúan sobre un objeto, con campos `force` y `torque`, ambos de tipo `Vector3`.

  - **sensor_msgs**: Mensajes relacionados con sensores.

    * **sensor_msgs/LaserScan**
      - Representa los datos de un escáner láser (LiDAR).
      - Incluye información sobre el ángulo mínimo y máximo de escaneo, el rango mínimo y máximo de detección, el ángulo entre mediciones consecutivas, y una lista de distancias medidas (rangos).
      - *Ejemplo de uso*: Para recibir datos de un sensor LiDAR en un robot móvil.
      ```
      sensor_msgs/LaserScan {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_laser"},
        angle_min: -1.57,
        angle_max: 1.57,
        angle_increment: 0.01,
        time_increment: 0.0,
        scan_time: 0.0,
        range_min: 0.1,
        range_max: 10.0,
        ranges: [0.5, 0.6, 0.7, ...]
      }
      ```

    * **sensor_msgs/Imu**
      - Representa datos de una unidad de medida inercial (IMU).
      - Incluye datos de orientación (como cuaterniones), aceleración lineal y velocidad angular (tasa de giro).
      - Ejemplo de uso: Para recibir datos de un IMU en un dron o robot móvil.
      ```
      sensor_msgs/Imu {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "imu_link"},
        orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0},
        orientation_covariance: [0.0, 0.0, 0.0, ...],
        angular_velocity: {x: 0.1, y: -0.2, z: 0.3},
        angular_velocity_covariance: [0.0, 0.0, 0.0, ...],
        linear_acceleration: {x: 0.4, y: -0.5, z: 0.6},
        linear_acceleration_covariance: [0.0, 0.0, 0.0, ...]
      }
      ```
    * **sensor_msgs/CameraInfo**
      - Proporciona información sobre la configuración de una cámara, como la matriz de la cámara, el tamaño de la imagen y los coeficientes de distorsión.
      - *Ejemplo de uso*: Para enviar datos sobre la calibración de una cámara.
      ```
      sensor_msgs/CameraInfo {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "camera_frame"},
        height: 720,
        width: 1280,
        distortion_model: "plumb_bob",
        D: [0.1, -0.1, 0.0, 0.0, 0.0],
        K: [1000.0, 0.0, 640.0, ...],
        R: [1.0, 0.0, 0.0, ...],
        P: [1000.0, 0.0, 640.0, ...],
        binning_x: 1,
        binning_y: 1,
        roi: {x_offset: 0, y_offset: 0, height: 720, width: 1280, do_rectify: false}
      }
      ```
    * **sensor_msgs/PointCloud2**
      - Representa un conjunto de puntos tridimensionales (nube de puntos).
      - Se utiliza para representar datos de escaneo de superficies u objetos en 3D, por ejemplo, de un sensor LiDAR o de una cámara de profundidad.
      - *Ejemplo de uso*: Para enviar datos de una nube de puntos capturados por un sensor.
      ```
      sensor_msgs/PointCloud2 {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "base_link"},
        height: 1,
        width: 1000,
        fields: [{name: "x", offset: 0, datatype: 7, ...}, ...],
        point_step: 32,
        row_step: 32000,
        data: [...],
        is_bigendian: false,
        is_dense: true
      }
      ```

  - **nav_msgs**: Mensajes relacionados con la navegación robótica.
    * **nav_msgs/Odometry**
      - Representa datos de odometría, que describen la posición y orientación actual de un robot, así como sus velocidades lineales y angulares.
      - Incluye un `header` con un sello de tiempo y un marco de referencia (`frame_id`).
      - Contiene una `PoseWithCovariance` (pose con información de incertidumbre) y una `TwistWithCovariance` (velocidad con información de incertidumbre).
      ```
      nav_msgs/Odometry {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "odom"},
        child_frame_id: "base_link",
        pose: {
            pose: {position: {x: 1.0, y: 2.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}},
            covariance: [0.1, 0.0, 0.0, ...]
        },
        twist: {
            twist: {linear: {x: 0.5, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 0.1}},
            covariance: [0.1, 0.0, 0.0, ...]
        }
      }
      ```

    * **nav_msgs/Path**
      - Representa un camino o trayectoria que un robot puede seguir para navegar a través de un espacio.
      - Consiste en una lista de poses (`PoseStamped`) a lo largo de una trayectoria planificada.
      - *Ejemplo de uso*: Para especificar una ruta de navegación para un robot.
      ```
      nav_msgs/Path {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
        poses: [
            {header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
            pose: {position: {x: 1.0, y: 1.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}},
            {header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
            pose: {position: {x: 2.0, y: 2.0, z: 0.0}, orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}}}
            // ...
        ]
      }
      ```

    * **nav_msgs/OccupancyGrid**
      - Representa un mapa de ocupación, que es una representación de un entorno en una cuadrícula bidimensional.
      - Cada celda de la cuadrícula contiene un valor que indica si está libre, ocupada o desconocida.
      - *Ejemplo de uso*: Para compartir un mapa de ocupación de un entorno con otros nodos o para planificar rutas.
      ```
      nav_msgs/OccupancyGrid {
        header: {stamp: {sec: 0, nanosec: 0}, frame_id: "map"},
        info: {
            map_load_time: {sec: 0, nanosec: 0},
            resolution: 0.05,
            width: 100,
            height: 100,
            origin: {
                position: {x: -2.5, y: -2.5, z: 0.0},
                orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
            }
        },
        data: [0, 100, -1, ...] // Valores de ocupación para cada celda
      }
      ```

    * **nav_msgs/MapMetaData**
      - Proporciona metadatos sobre un mapa, como la resolución, el tamaño y la posición de la cuadrícula de ocupación.
      - Se usa en conjunto con mensajes como `OccupancyGrid`.
      ```
      nav_msgs/MapMetaData {
        map_load_time: {sec: 0, nanosec: 0},
        resolution: 0.05,
        width: 100,
        height: 100,
        origin: {
            position: {x: -2.5, y: -2.5, z: 0.0},
            orientation: {x: 0.0, y: 0.0, z: 0.0, w: 1.0}
        }
    }
      ```
2. **Tipos de mensajes personalizados**: Además de los tipos de mensajes estándar, puedes definir tus propios tipos de mensajes personalizados para adaptarte a las necesidades específicas de tu aplicación. Los mensajes personalizados se crean utilizando el lenguaje de definición de mensajes (IDL) de ROS 2.

3. **Tipos de mensajes de servicios y acciones**: Además de los mensajes de tópicos, ROS 2 también tiene mensajes de servicios (srv) y acciones (action). Los servicios definen un tipo de solicitud y un tipo de respuesta, mientras que las acciones son una combinación de mensajes de objetivos, actualizaciones de estado y resultados.

4. **Mensajes de paquetes de terceros**: Además de los paquetes estándar, existen otros paquetes de ROS 2 desarrollados por la comunidad que proporcionan más tipos de mensajes para diferentes aplicaciones, como robótica, automoción, drones, etc.




### Comandos básicos
1. Para ver los topicos de los nodos `turtlesim` y `teleop_key` que previamente deben estar ejecución usamos la siguiente instrucción

```bash
ros2 topic list
```

Esto nos indica que deben estar ejecutándose estos tópicos.
```
  /parameter_events
  /rosout
  /turtle1/cmd_vel
  /turtle1/color_sensor
  /turtle1/pose
```

> **Nota**: Los tópicos `/parameter_events` y `/rosout` son de la ejecución de ROS2 y no pertenecen a los paquetes y nodos en ejecución, por lo tanto, siempre van a estar presentes.

2. Otra herramienta útil para el desarrollo de los tópicos con ROS2 es saber el tipo de los tópicos.
```bash
ros2 topic list -t
```
Y nos muestra la siguiente información.
```
  /parameter_events [rcl_interfaces/msg/ParameterEvent]
  /rosout [rcl_interfaces/msg/Log]
  /turtle1/cmd_vel [geometry_msgs/msg/Twist]
  /turtle1/color_sensor [turtlesim/msg/Color]
  /turtle1/pose [turtlesim/msg/Pose]
```

3. Durante la instalación, se descargó una herramienta útil para visualizar la conexión de los nodos, tópicos, servicios y acciones de nuestro proyecto. Para visualizar la arquitectura del proyecto, podemos usar el comando.
```bash
rqt_graph
```
Y nos habilita la ventana para ver el **rqt_graph**.
<div id="header" align="center">
    <img src="/images/rqt_graph.PNG" alt="rqt_graph" width="50%" max-width="100%">
</div>

4. Para visualizar el flujo de información de un tópico `cmd_vel` usamos el siguiente comando.
```bash
ros2 topic echo  /turtle1/cmd_vel
```
Esto nos habilitará información enviada a travás del tópico `/turtle/cmd_vel`.

```
  linear:
    x: 2.0
    y: 0.0
    z: 0.0
  angular:
    x: 0.0
    y: 0.0
    z: 0.0
  ---
```

5. Tambien podemos ver la información del tópico pose `pose`.
```bash
ros2 topic echo  /turtle1/pose
```
Nos imprimira la posición y ángulo de la tortuga.
```
  x: 5.544444561004639
  y: 5.544444561004639
  theta: 0.0
  linear_velocity: 0.0
  angular_velocity: 0.0
  ---
```

6. En el caso de querer ver la información de un tópico usamos:
```bash
ros2 topic info /turtle1/cmd_vel
```

Lo cual nos retorna el tipo de nodo, número de nodos suscritos y número de nodos publicando.
```
  Type: geometry_msgs/msg/Twist
  Publisher count: 1
  Subscription count: 1
```

7. Ver la extructura de mensaje enviada en el tópico.
```bash
ros2 interface show geometry_msgs/msg/Twist
```
Retorna la extructura.
```
  # This expresses velocity in free space broken into its linear and angular parts.

  Vector3  linear
          float64 x
          float64 y
          float64 z
  Vector3  angular 
          float64 x
          float64 y
          float64 z
```
8. Publicar información a través del tópico.
```bash
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0, y: 0.0, z: 0.0},
angular: {x: 0.0, y: 0.0, z: 1.5}}"
```

9. Publicar información a través del tópico con una determinada frecuencia.
```bash
ros2 topic pub --rate /turtle1/cmd_vel geometry_msgs/msg/Twist "{linear: {x: -2.0, y: 0.0, z: 0.0},
angular: {x: 0.0, y: 0.0, z: 1.5}}"
```
10. Para visualizar la frecuencia con la que un nodo publica.
```bash
ros2 topic hz /turtle1/cmd_vel
```
Retorna la velocidad de publicación.
```
  average rate: 0.200
          min: 4.999s max: 5.001s std dev: 0.00058s window: 2
  average rate: 0.200
          min: 4.999s max: 5.001s std dev: 0.00070s window: 3
  average rate: 0.200
          min: 4.999s max: 5.001s std dev: 0.00090s window: 4
  average rate: 0.200
```

<br>

## SERVICIOS

<div align="center">
    <img src="/images/services_diagram.svg" alt="Diagrama de Servicios" width="70%" max-width="100%">
</div>

En ROS 2, los servicios son un mecanismo de comunicación que permite a los nodos intercambiar datos de forma *síncrona*. A través de los servicios, un nodo (el servidor) puede ofrecer una funcionalidad específica que otros nodos (los clientes) pueden solicitar. Cuando un cliente hace una solicitud a un servicio, espera una respuesta inmediata del servidor. Esto es diferente de los temas (o topics), que son de naturaleza *asíncrona*.

Un servicio en ROS 2 tiene tres componentes principales:

1. **Definición del servicio**: Similar a los mensajes, los servicios también tienen su propio tipo de definición, que incluye tanto los datos de la solicitud (request) como los datos de la respuesta (response).

2. **Nodo servidor**: Es el nodo que implementa la funcionalidad del servicio. Escucha las solicitudes de los nodos clientes y, cuando recibe una, realiza la operación solicitada y responde con los datos apropiados.

3. **Nodo cliente**: Es el nodo que solicita la funcionalidad proporcionada por el servidor. Realiza una llamada al servicio y espera una respuesta.

Este patrón de solicitud-respuesta es útil para cuando se necesita una interacción puntual y sincrónica entre nodos, en contraste con el modelo de publicación-suscripción que es más adecuado para comunicaciones asíncronas y continuas.

### Clasificación

1. **Servicios estándar**:
En ROS2, hay varios servicios estándar que forman parte de los paquetes básicos de ROS2 y proporcionan funcionalidad común que es útil para muchas aplicaciones.
    - **Servicios básicos (std_srvs)**:
      * **Empty**: Un servicio sin datos de solicitud ni de respuesta.
      * **SetBool**: Servicio que toma un valor booleano como solicitud y devuelve un valor booleano y una cadena de respuesta.
      * **Trigger**: Servicio que no tiene datos de solicitud, pero devuelve un valor.
    - **Servicios de interfaces del sistema (rcl_interfaces)**:
      * **SetParameters**: Permite configurar los parámetros de un nodo.
      * **GetParameters**: Permite obtener los parámetros de un nodo específico.
      * **GetParameterTypes**: Permite obtener los tipos de parámetros de un nodo.
      * **DescribeParameters**: Ofrece información sobre los parámetros de un nodo, incluidos los descriptores.
      * **ListParameters**: Proporciona una lista de los parámetros disponibles en un nodo.
    - **Servicios de la biblioteca de imagen (image_transport)**:
      * **GetTransportInfo**:  Servicio que proporciona información sobre los transportes de imágenes disponibles.
    - **Servicios de transformación (tf2_msgs)**
      * **LookupTransform**: Proporciona información sobre las transformaciones de coordenadas.

2. **Servicios no estándar**:
Los servicios no estándar son aquellos definidos por los desarrolladores para aplicaciones específicas. Estos servicios pueden variar ampliamente según el ámbito de la aplicación, el paquete ROS 2 utilizado y los requerimientos del sistema. Los archivos .srv dentro de los paquetes describen los servicios específicos.


### Comandos básicos

1. Listar servicios.
```bash
ros2 service list
```
Retorna
```
  /clear
  /kill
  /reset
  /spawn
  /teleop_turtle/describe_parameters
  /teleop_turtle/get_parameter_types
  /teleop_turtle/get_parameters
  /teleop_turtle/list_parameters
  /teleop_turtle/set_parameters
  /teleop_turtle/set_parameters_atomically
  /turtle1/set_pen
  /turtle1/teleport_absolute
  /turtle1/teleport_relative
  /turtlesim/describe_parameters
  /turtlesim/get_parameter_types
  /turtlesim/get_parameters
  /turtlesim/list_parameters
  /turtlesim/set_parameters
  /turtlesim/set_parameters_atomically
```

2. Ver el tipo de los servicios.
```bash
ros2 service list -t
```
Retorna
```
  /clear [std_srvs/srv/Empty]
  /kill [turtlesim/srv/Kill]
  /reset [std_srvs/srv/Empty]
  /spawn [turtlesim/srv/Spawn]
  /teleop_turtle/describe_parameters [rcl_interfaces/srv/DescribeParameters]
  /teleop_turtle/get_parameter_types [rcl_interfaces/srv/GetParameterTypes]
  /teleop_turtle/get_parameters [rcl_interfaces/srv/GetParameters]
  /teleop_turtle/list_parameters [rcl_interfaces/srv/ListParameters]
  /teleop_turtle/set_parameters [rcl_interfaces/srv/SetParameters]
  /teleop_turtle/set_parameters_atomically [rcl_interfaces/srv/SetParametersAtomically]
  /turtle1/set_pen [turtlesim/srv/SetPen]
  /turtle1/teleport_absolute [turtlesim/srv/TeleportAbsolute]
  /turtle1/teleport_relative [turtlesim/srv/TeleportRelative]
  /turtlesim/describe_parameters [rcl_interfaces/srv/DescribeParameters]
  /turtlesim/get_parameter_types [rcl_interfaces/srv/GetParameterTypes]
  /turtlesim/get_parameters [rcl_interfaces/srv/GetParameters]
  /turtlesim/list_parameters [rcl_interfaces/srv/ListParameters]
  /turtlesim/set_parameters [rcl_interfaces/srv/SetParameters]
  /turtlesim/set_parameters_atomically [rcl_interfaces/srv/SetParametersAtomically]
```

3. Ver el tipo de un servicio en específico.
```bash
ros2 service type /clear
```
El tipo de servicio es un servicio estandar vacio.
```
  std_srvs/srv/Empty
```

4. Visualizar si los servicios de algún tipo están ejecutándose.
```bash
ros2 service find std_srvs/srv/Empty
```
En este caso tenemos dos servicios de este tipo.
```
  /clear
  /reset
```

5. Para llamar y usar un servicio.
```bash
ros2 service call /clear std_srvs/srv/Empty
```
Retorna valores de la solicitud
```
  requester: making request: std_srvs.srv.Empty_Request()

  response:
  std_srvs.srv.Empty_Response()
```

6. Para ver la estructura del `request` y el `response`.
```bash
ros2 interface show turtlesim/srv/Spawn
```
Retorna
```
  float32 x
  float32 y
  float32 theta
  string name # Optional.  A unique name will be created and returned if this is empty
  ---
  string name
```


7. Llamar el servicio Spawn
```bash
ros2 service call /spawn turtlesim/srv/Spawn "{x: 2, y: 2, theta: 0.2, name: 'tortuga_mario'}"
```
Retorna en consola y dibuja una segunda tortuga.
```
requester: making request: turtlesim.srv.Spawn_Request(x=2.0, y=2.0, theta=0.2, name='tortuga_mario')

response:
turtlesim.srv.Spawn_Response(name='tortuga_mario')
```

<br>

## ACCIONES

<div align="center">
    <img src="/images/actions_diagram.svg" alt="Diagrama de Acciones" width="75%" max-width="100%">
</div>

Las acciones en ROS 2 permiten a los nodos ejecutar tareas complejas de forma asíncrona, con retroalimentación y capacidad de cancelación. Son útiles para operaciones que requieren tiempo y seguimiento.

Una acción tiene tres componentes:

1. **Goal**: El objetivo que el cliente envía al servidor.
2. **Result**: El resultado final que el servidor devuelve al cliente.
3. **Feedback**: Información intermedia que el servidor envía al cliente durante la ejecución.


### Tipos de Acciones

- **Simple**: Se envía un solo objetivo, el servidor procesa y devuelve un resultado.
- **Compuesta**: Involucra varios pasos o sub-tareas secuenciales, con feedback entre cada uno.

### Sistemas

- **actionlib**: Sistema de acciones de ROS 1, compatible en ROS 2 mediante un puente.
- **rcl_action**: Sistema nativo de ROS 2, más eficiente y flexible.


### Comandos
Ejecutar el nodo `turtle_teleop_key`, el cual permite controlar la tortuga:
```bash
ros2 run turtlesim turtle_teleop_key
```
Al controlar la tortuga con el teclado, podremos ver en la consola del nodo  `turtlesim_node` las acciones.

```
axioma@axioma-ThinkPad-E14:~$ ros2 run turtlesim turtlesim_node 

  Warning: Ignoring XDG_SESSION_TYPE=wayland on Gnome. Use QT_QPA_PLATFORM=wayland to run on Wayland anyway.
  [INFO] [1727503174.349438896] [turtlesim]: Starting turtlesim with node name /turtlesim
  [INFO] [1727503174.354274238] [turtlesim]: Spawning turtle [turtle1] at x=[5.544445], y=[5.544445], theta=[0.000000]
  [INFO] [1727503191.485609711] [turtlesim]: Rotation goal completed successfully
  [INFO] [1727503194.604274960] [turtlesim]: Rotation goal canceled
  [WARN] [1727503201.052657946] [turtlesim]: Rotation goal received before a previous goal finished. Aborting previous goal
  [INFO] [1727503202.396488251] [turtlesim]: Rotation goal completed successfully

```
Revisanmos la información del nodo `turtlesim_node`:
```bash
ros2 node info /turtlesim
```
Esta es la arquitectura del nodo:
```
/turtlesim
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/color_sensor: turtlesim/msg/Color
    /turtle1/pose: turtlesim/msg/Pose
  Service Servers:
    /clear: std_srvs/srv/Empty
    /kill: turtlesim/srv/Kill
    /reset: std_srvs/srv/Empty
    /spawn: turtlesim/srv/Spawn
    /turtle1/set_pen: turtlesim/srv/SetPen
    /turtle1/teleport_absolute: turtlesim/srv/TeleportAbsolute
    /turtle1/teleport_relative: turtlesim/srv/TeleportRelative
    /turtlesim/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /turtlesim/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /turtlesim/get_parameters: rcl_interfaces/srv/GetParameters
    /turtlesim/list_parameters: rcl_interfaces/srv/ListParameters
    /turtlesim/set_parameters: rcl_interfaces/srv/SetParameters
    /turtlesim/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
  Action Clients:
```
Es importante destacar que este nodo contiene un `Action server`
```
Action Servers:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```

Ahora, si se inspecciona el nodo `turtle_teleop_key`
```bash
ros2 node info /teleop_turtle 
```
Y podemos revisar la arquitectura del nodo:
```
/teleop_turtle
  Subscribers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
  Publishers:
    /parameter_events: rcl_interfaces/msg/ParameterEvent
    /rosout: rcl_interfaces/msg/Log
    /turtle1/cmd_vel: geometry_msgs/msg/Twist
  Service Servers:
    /teleop_turtle/describe_parameters: rcl_interfaces/srv/DescribeParameters
    /teleop_turtle/get_parameter_types: rcl_interfaces/srv/GetParameterTypes
    /teleop_turtle/get_parameters: rcl_interfaces/srv/GetParameters
    /teleop_turtle/list_parameters: rcl_interfaces/srv/ListParameters
    /teleop_turtle/set_parameters: rcl_interfaces/srv/SetParameters
    /teleop_turtle/set_parameters_atomically: rcl_interfaces/srv/SetParametersAtomically
  Service Clients:

  Action Servers:

  Action Clients:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```
En este caso, el nodo tiene un `Action client`
```
  Action Clients:
    /turtle1/rotate_absolute: turtlesim/action/RotateAbsolute
```

**Otros comandos importantes**
1. Listar acciones
```bash
ros2 action list
```
En consola se listan las acciones en ejecución
```
/turtle1/rotate_absolute
```

2. Listar acciones y el tipo
```bash
ros2 action list -t
```
En consola observamos las acciones y el tipo:
```
/turtle1/rotate_absolute [turtlesim/action/RotateAbsolute]
```

3. Ver informacion de una accion
```bash
ros2 action info /turtle1/rotate_absolute
```
En este caso se observaran el servidor y los clientes:
```
Action: /turtle1/rotate_absolute
Action clients: 1
    /teleop_turtle
Action servers: 1
    /turtlesim
```

4. Ver interfaz de la acción
```bash
ros2 interface show turtlesim/action/RotateAbsolute
```
Con esto observamos la estructura de los datos de la acción
```
# The desired heading in radians
float32 theta
---
# The angular displacement in radians to the starting position
float32 delta
---
# The remaining rotation in radians
float32 remaining
```
5. Usar la acción acción
```bash
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.72}"
```
Con esto enviamos a través de la acción en radianes el nuevo angulo de la tortuga
```
Waiting for an action server to become available...
Sending goal:
     theta: 1.72

Goal accepted with ID: 0932fbe8ea15419ba192ac3f1b6111aa

Result:
    delta: -0.4000000059604645

Goal finished with status: SUCCEEDED
```

6. Visualiza el feedback
```bash
ros2 action send_goal /turtle1/rotate_absolute turtlesim/action/RotateAbsolute "{theta: 1.72}" --feedback
```
Podemos ver los datos del feedback
```
Feedback:
    remaining: 0.10399997234344482
Feedback:
    remaining: 0.08799993991851807
Feedback:
    remaining: 0.07200002670288086
Feedback:
    remaining: 0.0559999942779541
Feedback:
    remaining: 0.039999961853027344
Feedback:
    remaining: 0.023999929428100586
Feedback:
    remaining: 0.008000016212463379
Result:
    delta: -2.8480000495910645

Goal finished with status: SUCCEEDED
```

## INTERFACES

<div align="center">
    <img src="/images/interfaces_diagram.svg" alt="Diagrama de Interfaces" width="75%" max-width="100%">
</div>

En ROS 2, las interfaces definen cómo se comunican los nodos entre sí mediante mensajes, servicios o acciones. Son plantillas que describen los datos que se intercambian en las comunicaciones.


### Tipos de Interfaces en ROS 2:

  1. **Mensajes (Messages)**: Definen los datos enviados en un tema (topic). Se usan para comunicaciones asíncronas.

      *Ejemplo*: `std_msgs/String` (mensaje con una cadena de texto).
      </br>
  2. **Servicios (Services)**: Permiten la comunicación sincrónica entre un cliente y un servidor, con una solicitud y una respuesta.

        *Ejemplo*: `std_srvs/SetBool` (envía un booleano y recibe una respuesta).
        </br>

  3. **Acciones (Actions)**: Extienden los servicios para operaciones que pueden llevar más tiempo, permitiendo enviar retroalimentación y resultados parciales mientras se ejecuta.

      *Ejemplo*: `action_msgs/GoalStatusArray` (monitorea el progreso de una acción).

### Clasificación:

  1. **Predefinidas**: ROS 2 incluye muchas interfaces listas para usar.

  2. **Personalizadas**: Los desarrolladores pueden crear sus propias interfaces según los requisitos de su aplicación.



  Las interfaces se definen en archivos `.msg`, `.srv`, o .`action`.
  ROS 2 utiliza DDS para gestionar la comunicación y garantizar el envío de datos de las interfaces entre los nodos.

### Comandos
1. Listar todas las interfaces:
```bash
ros2 interface list
```
2. Listar solo las interfaces de acciones:
```bash
ros2 interface list | grep action
```
3. Mostrar los detalles de una interfaz de acción:
```bash
ros2 interface show turtlesim/action/RotateAbsolute
```
4. Mostrar la interfaz de un mensaje o servicio específico.
- Para mensajes:
```bash
ros2 interface show geometry_msgs/msg/Twist
```
- Para servicios:
```bash
ros2 interface show turtlesim/srv/TeleportAbsolute
```

## PARAMETROS

<div align="center">
    <img src="/images/parameters_diagram.svg" alt="Diagrama de Parámetros" width="70%" max-width="100%">
</div>

Los parámetros en ROS 2 son valores de configuración de los nodos que pueden ser modificados en tiempo de ejecución sin necesidad de recompilar el código. Cada nodo puede declarar y usar sus propios parámetros. Los tipos soportados son: `integer`, `float`, `string`, `boolean`, `byte array` y listas.

### Comandos básicos

Asegúrate de tener los nodos `turtlesim_node` y `turtle_teleop_key` en ejecución.

1. Listar los parámetros de todos los nodos.
```bash
ros2 param list
```
Retorna los parámetros de cada nodo en ejecución.
```
/teleop_turtle:
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  scale_angular
  scale_linear
  use_sim_time
/turtlesim:
  background_b
  background_g
  background_r
  qos_overrides./parameter_events.publisher.depth
  qos_overrides./parameter_events.publisher.durability
  qos_overrides./parameter_events.publisher.history
  qos_overrides./parameter_events.publisher.reliability
  use_sim_time
```

2. Obtener el valor de un parámetro específico.
```bash
ros2 param get /turtlesim background_g
```
Retorna el valor y tipo del parámetro.
```
Integer value is: 86
```

3. Establecer un nuevo valor a un parámetro. Por ejemplo, cambiar el color de fondo del `turtlesim`.
```bash
ros2 param set /turtlesim background_r 150
```
Retorna confirmación del cambio.
```
Set parameter successful
```
> **Nota**: El cambio es inmediato, el fondo del turtlesim cambiará de color al instante. Sin embargo, este cambio no persiste si reinicias el nodo.

4. Ver todos los parámetros de un nodo con sus valores.
```bash
ros2 param dump /turtlesim
```
Retorna todos los parámetros en formato YAML.
```
/turtlesim:
  ros__parameters:
    background_b: 255
    background_g: 86
    background_r: 150
    qos_overrides:
      /parameter_events:
        publisher:
          depth: 1000
          durability: volatile
          history: keep_last
          reliability: reliable
    use_sim_time: false
```

5. Guardar los parámetros actuales en un archivo YAML.
```bash
ros2 param dump /turtlesim >> turtlesim_params.yaml
```

6. Cargar parámetros desde un archivo YAML al iniciar un nodo.
```bash
ros2 run turtlesim turtlesim_node --ros-args --params-file turtlesim_params.yaml
```
> Esto es útil para restaurar configuraciones personalizadas sin tener que establecer cada parámetro manualmente.

7. Describir un parámetro (ver tipo, descripción y restricciones).
```bash
ros2 param describe /turtlesim background_r
```
Retorna información detallada.
```
Parameter name: background_r
  Type: integer
  Description: Red channel of the background color
  Constraints:
    Min value: 0
    Max value: 255
    Step: 0
```

<br>

## LAUNCH

<div align="center">
    <img src="/images/launch_diagram.svg" alt="Diagrama de Launch" width="70%" max-width="100%">
</div>

En ROS 2, los launch files (archivos de lanzamiento) son scripts que se utilizan para iniciar y configurar nodos y sistemas completos. Estos archivos permiten ejecutar varios nodos simultáneamente, establecer parámetros, definir remapeos de temas y configurar acciones o servicios, todo en un solo comando.

### Características principales:

  1. **Lenguaje**: Los launch files en ROS 2 están escritos en Python.
  Modularidad: Permiten lanzar múltiples nodos a la vez.
  2. **Configuración**: Puedes establecer parámetros, remapear temas y configurar dependencias entre nodos.
  3. **Reusabilidad**: Se pueden crear composiciones de nodos y reutilizar archivos launch en diferentes proyectos.

### Comando
```bash
ros2 launch <nombre_paquete> <archivo_launch.py>
```

### Ejemplo: Lanzar turtlesim con teleop en un solo comando

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Nodo de turtlesim_node
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim',
            output='screen'
        ),
        # Nodo de turtle_teleop_key
        Node(
            package='turtlesim',
            executable='turtle_teleop_key',
            name='teleop_turtle',
            output='screen'
        )
    ])
```

### Configuracion del launch en el paquete

1. **En C++**: Agregar al `CMakeLists.txt`:

    ```cmake
    install(
    DIRECTORY launch
    DESTINATION share/${PROJECT_NAME}
    )
    ```

2. **En Python**: Agregar al `setup.py`:

    ```python
    data_files=[
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    ```

<br>

---

## VIRTUALIZACIÓN DE UN ROBOT

En ROS (Robot Operating System), el **URDF** (Unified Robot Description Format) es un formato de archivo XML utilizado para describir la geometría del robot, es decir, su estructura física, en términos de enlaces (**links**) y juntas (**joints**). Los enlaces representan las partes sólidas del robot (como **eslabones o piezas**), mientras que las juntas describen cómo estos enlaces están conectados y pueden moverse entre sí (como **articulaciones rotativas o prismáticas**).

<div align="center">
    <img src="/images/urdf_diagram.svg" alt="Diagrama URDF" width="85%" max-width="100%">
</div>

El **Xacro** es una extensión de XML utilizada para escribir URDF de manera más eficiente y modular. Permite la reutilización de código y la parametrización de modelos, lo que simplifica la descripción y mantenimiento de robots complejos.

El **SDF** (Simulation Description Format) es un formato de archivo XML utilizado en el simulador Gazebo. Describe tanto la geometría como la física de los modelos de robots y entornos de simulación. Mientras que el URDF y el Xacro se centran en la geometría y la cinemática del robot, el SDF agrega información adicional necesaria para la simulación, como propiedades de los materiales, colisiones y restricciones físicas.

| Elemento              | Descripción                                                      | Ejemplo de Uso                                               |
|-----------------------|------------------------------------------------------------------|-------------------------------------------------------------|
| **`<robot>`**         | Elemento raíz que define el robot.                              | `<robot name="mi_robot">`                                   |
| **`<link>`**          | Define un link del robot, que representa una parte rígida.      | `<link name="base_link">`                                   |
| **`<joint>`**         | Define la conexión entre dos links y su tipo de movimiento.     | `<joint name="joint1" type="revolute">`                   |
| **`<origin>`**        | Especifica la posición y orientación del link o joint.          | `<origin xyz="0 0 0.1" rpy="0 0 0"/>`                      |
| **`<parent>`**        | Define el link padre en un joint.                               | `<parent link="base_link"/>`                                |
| **`<child>`**         | Define el link hijo en un joint.                                | `<child link="link1"/>`                                     |
| **`<visual>`**        | Define la representación visual del link.                       | `<visual><geometry><box size="0.1 0.1 0.1"/></geometry></visual>` |
| **`<collision>`**     | Define la geometría para las colisiones.                        | `<collision><geometry><cylinder radius="0.05" length="0.1"/></geometry></collision>` |
| **`<sensor>`**        | Define un sensor asociado al link.                              | `<sensor name="my_sensor" type="camera">...</sensor>`      |
| **`<material>`**      | Define las propiedades de material, como color.                 | `<material name="red_material"><color rgba="1 0 0 1"/></material>` |
| **`<include>`**       | Permite incluir otros archivos URDF dentro del archivo actual.  | `<include filename="otro_robot.urdf"/>`                    |
| **`<transmission>`**  | Define cómo el movimiento se transmite entre los joints y motores. | `<transmission name="transmission1"><actuator name="motor1"/><joint name="joint1"/></transmission>` |

<br>

---

## Guías complementarias

| Guía | Descripción |
|------|-------------|
| [Instalación](./INSTALL.md) | Instalación de ROS 2 Humble en Ubuntu |
| [Simulador Turtlesim](./turtlesim/) | Configuración e instalación de turtlesim |
| [Crear paquetes en ROS 2](./src/) | Cómo crear paquetes con ament_cmake y ament_python |
| [Referencia Python (rclpy)](./NotasPY.md) | API de ROS 2 con Python + POO |
| [Referencia C++ (rclcpp)](./NotasCPP.md) | API de ROS 2 con C++ + POO + Ejemplos prácticos |
