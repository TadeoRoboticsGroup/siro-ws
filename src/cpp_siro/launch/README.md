# Launch files en ROS 2

Los launch files permiten iniciar y coordinar multiples nodos con un solo comando. Se escriben en Python y definen que nodos lanzar, con que parametros y configuracion.

### [`↩️ Volver al paquete`](../README.md) | [`↩️ Inicio`](../../../README.md)

---

## Estructura de un launch file

```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='nombre_paquete',
            executable='nombre_ejecutable',
            name='nombre_nodo',
            output='screen',
            parameters=[{'param1': valor1}]
        ),
        # Mas nodos...
    ])
```

### Componentes principales

| Componente | Funcion |
|------------|---------|
| `LaunchDescription` | Contenedor de todos los nodos y acciones a lanzar |
| `Node` | Define un nodo con su paquete, ejecutable, nombre y parametros |
| `generate_launch_description()` | Funcion requerida, punto de entrada del launch |

---

## Ejemplo: siro_urdf_launch.py

Este launch inicia un URDF con `robot_state_publisher`, `joint_state_publisher_gui` y `rviz2`:

```python
import launch
import launch_ros.actions
import os
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    package_dir = get_package_share_directory('cpp_siro')
    urdf_file = os.path.join(package_dir, 'urdf', 'siro_urdf.xml')

    joint_state_publisher_node = launch_ros.actions.Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
    )

    robot_state_publisher_node = launch_ros.actions.Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        parameters=[{'robot_description': open(urdf_file).read()}],
    )

    rviz2_node = launch_ros.actions.Node(
        package="rviz2",
        executable="rviz2",
        arguments=["-d", os.path.join(package_dir, 'rviz', 'default.rviz')],
    )

    return launch.LaunchDescription([
        joint_state_publisher_node,
        robot_state_publisher_node,
        rviz2_node,
    ])
```

### Ejecutar
```bash
ros2 launch cpp_siro siro_urdf_launch.py
```

---

## Parametros utiles de Node

| Parametro | Descripcion | Ejemplo |
|-----------|-------------|---------|
| `package` | Nombre del paquete | `'turtlesim'` |
| `executable` | Nombre del ejecutable | `'turtlesim_node'` |
| `name` | Nombre del nodo (override) | `'mi_turtle'` |
| `output` | Salida del log | `'screen'` |
| `parameters` | Lista de parametros | `[{'use_sim_time': True}]` |
| `remappings` | Remapeo de topics | `[('/cmd_vel', '/turtle1/cmd_vel')]` |
| `arguments` | Argumentos CLI | `['-d', 'config.rviz']` |

---

### [`↩️ Volver al paquete`](../README.md) | [`↩️ Inicio`](../../../README.md)
