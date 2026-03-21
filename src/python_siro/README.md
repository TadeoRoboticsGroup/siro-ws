# Paquete python_siro (ament_python)

Paquete de ejemplo en Python para ROS 2.

### [`↩️ Volver a paquetes`](../README.md) | [`↩️ Inicio`](../../README.md)

---

## Estructura del paquete

```
python_siro/
  ├── setup.py              # Configuracion del paquete
  ├── setup.cfg             # Entry points de scripts
  ├── package.xml           # Metadatos y dependencias
  ├── python_siro/          # Modulo Python
  │   ├── __init__.py
  │   └── mi_nodo.py        # Nodo principal
  ├── launch/               # Archivos de lanzamiento
  └── config/               # Configuracion
```

## Crear el paquete

```bash
cd ~/siro_ws/src
ros2 pkg create --build-type ament_python --node-name mi_nodo python_siro
```

---

## Configuracion de setup.py

```python
from setuptools import setup

package_name = 'python_siro'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='tu_nombre',
    maintainer_email='tu_email@example.com',
    description='Paquete Python de ejemplo para ROS 2',
    license='Apache License 2.0',
    entry_points={
        'console_scripts': [
            'mi_nodo = python_siro.mi_nodo:main',
        ],
    },
)
```

> Para agregar archivos launch, agregar a `data_files`:
> ```python
> (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
> ```

---

## Ejemplo de nodo basico

```python
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MiNodo(Node):
    def __init__(self):
        super().__init__('mi_nodo')
        self.publisher_ = self.create_publisher(String, 'mi_topico', 10)
        self.timer = self.create_timer(1.0, self.timer_callback)
        self.get_logger().info('Nodo iniciado')

    def timer_callback(self):
        msg = String()
        msg.data = 'Hola desde python_siro'
        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = MiNodo()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

---

## Compilar y ejecutar

```bash
cd ~/siro_ws
colcon build --packages-select python_siro
source install/setup.bash
ros2 run python_siro mi_nodo
```

---

## Archivos principales

| Archivo | Funcion |
|---------|---------|
| `setup.py` | Nombre, version, entry points (nodos ejecutables) |
| `setup.cfg` | Directorio donde se instalan los scripts |
| `package.xml` | Dependencias de ROS 2 (rclpy, std_msgs, etc.) |
| `python_siro/__init__.py` | Marca el directorio como modulo Python |
| `python_siro/mi_nodo.py` | Codigo del nodo |

---

### [`↩️ Volver a paquetes`](../README.md) | [`↩️ Inicio`](../../README.md)
