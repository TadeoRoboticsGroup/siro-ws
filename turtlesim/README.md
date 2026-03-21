# Turtlesim

Turtlesim es un simulador 2D incluido en ROS 2 que permite controlar una tortuga virtual. Es la herramienta principal para aprender los conceptos basicos de ROS 2 (nodos, topics, services y actions) de forma practica.

<div align="center">
    <img src="/images/turtlesim_node.png" alt="Turtlesim" width="50%" max-width="100%">
</div>

### [`↩️ Volver al inicio`](../README.md)

---

## Instalacion

```bash
sudo apt install ros-humble-turtlesim
```

Verificar que se instalo correctamente:
```bash
ros2 pkg executables turtlesim
```
Debe mostrar:
```
turtlesim draw_square
turtlesim mimic
turtlesim turtle_teleop_key
turtlesim turtlesim_node
```

---

## Arquitectura de Turtlesim

<div align="center">
    <img src="/images/turtlesim_architecture.svg" alt="Arquitectura Turtlesim" width="80%" max-width="100%">
</div>

---

## Comandos rapidos

### Iniciar turtlesim
```bash
# Terminal 1: Ventana grafica con la tortuga
ros2 run turtlesim turtlesim_node

# Terminal 2: Control con teclado
ros2 run turtlesim turtle_teleop_key
```

### Nodos
```bash
ros2 node list                    # Ver nodos activos
ros2 node info /turtlesim         # Detalle del nodo
```

### Topics
```bash
ros2 topic list                   # Listar topics
ros2 topic list -t                # Listar con tipos
ros2 topic echo /turtle1/pose     # Ver mensajes en tiempo real
ros2 topic info /turtle1/cmd_vel  # Info del topic
ros2 topic pub --once /turtle1/cmd_vel geometry_msgs/msg/Twist \
  "{linear: {x: 2.0, y: 0.0, z: 0.0}, angular: {x: 0.0, y: 0.0, z: 1.5}}"
```

### Services
```bash
ros2 service list                 # Listar servicios
ros2 service list -t              # Listar con tipos
ros2 service type /clear          # Ver tipo de servicio
ros2 service call /clear std_srvs/srv/Empty   # Limpiar rastro
ros2 service call /spawn turtlesim/srv/Spawn \
  "{x: 2, y: 2, theta: 0.2, name: 'turtle2'}"   # Crear tortuga
```

### Actions
```bash
ros2 action list                  # Listar acciones
ros2 action list -t               # Listar con tipos
ros2 action info /turtle1/rotate_absolute   # Info de la accion
ros2 action send_goal /turtle1/rotate_absolute \
  turtlesim/action/RotateAbsolute "{theta: 1.57}"            # Enviar goal
ros2 action send_goal /turtle1/rotate_absolute \
  turtlesim/action/RotateAbsolute "{theta: 1.57}" --feedback  # Con feedback
```

### Parameters
```bash
ros2 param list                           # Listar parametros
ros2 param get /turtlesim background_r    # Ver valor
ros2 param set /turtlesim background_r 200  # Cambiar color fondo
ros2 param dump /turtlesim                # Exportar todos los params
```

### Herramientas de visualizacion
```bash
rqt_graph         # Ver grafo de nodos y topics
rqt               # Panel de herramientas ROS 2
```

---

### [`↩️ Volver al inicio`](../README.md)
