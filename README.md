# 🎯PROYECTO ROS2 HUMBLE 🤖🚀🕹️


<!--div id="header" align="center" style="text-align: center; white-space: nowrap">
    <img src="/images/ros2.gif" title="ros2" alt="ros2" width="300px"/>
    <img src="/images/humble.png" title="humble" alt="humble" width="150px"/>
</div-->

<div id="header" align="center">
    <img src="/images/ros-image2.png" alt="ros humble" width="60%" max-width="100%">
</div>


ROS 2 (Robot Operating System 2) es una plataforma de código abierto diseñada para facilitar el desarrollo, operación y mantenimiento de sistemas robóticos y de automatización industrial. Ofrece una arquitectura modular y flexible que permite la comunicación entre componentes distribuidos, soportando una variedad de sistemas operativos y arquitecturas de hardware. ROS 2 se destaca por su capacidad de escalabilidad, seguridad y robustez, lo que lo convierte en una herramienta crucial para la creación de sistemas robóticos avanzados en diversos entornos industriales y de investigación.


## Preparación del espacio de trabajo


### Creación del proyecto Ros2


1. Creación del workspace.

### `mkdir -p siro_ws/src`

2. Ingresamos a `siro_ws`

### `cd siro_ws`

3. Compilación del proyecto

### `colcon build`


Al compilar se crean 3 direcorios nuevos
```
    \build
    \install
    \log
```

4. Actualizar las fuentes compiladas 

### `source install/setup.bash`


Realizar el paso 3 y 4 cada vez que se realice un cambio

## [`👉 Crea paquetes en ROS2`](./src/)

--

## Arquitectura ROS2


<div id="header" align="center">
    <img src="/images/arquitectura.png" alt="Descripción de la imagen" width="50%" max-width="100%">
</div>

## [`👉 Simulador Turtlesim`](./turtlesim/)




