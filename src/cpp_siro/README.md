# Paquete cpp_siro (ament_cmake)

Paquete de ejemplo en C++ con nodos publicador y suscriptor.

### [`↩️ Volver a paquetes`](../README.md) | [`↩️ Inicio`](../../README.md)

---

## Estructura del paquete

```
cpp_siro/
  ├── CMakeLists.txt        # Configuracion de compilacion
  ├── package.xml           # Metadatos y dependencias
  ├── src/                  # Codigo fuente
  │   ├── siro_node_publicador.cpp
  │   └── siro_node_suscriptor.cpp
  ├── include/              # Headers
  ├── launch/               # Archivos de lanzamiento
  │   └── siro_urdf_launch.py
  ├── urdf/                 # Modelos del robot
  └── config/               # Configuracion
```

## Crear el paquete

```bash
ros2 pkg create --build-type ament_cmake cpp_siro
cd cpp_siro
```

---

## Configuracion de CMakeLists.txt

### Version y nombre del proyecto
```cmake
cmake_minimum_required(VERSION 3.5)
project(cpp_siro)
```

### Version de C++
```cmake
if(NOT CMAKE_CXX_STANDARD)
    set(CMAKE_CXX_STANDARD 14)
endif()
```

### Dependencias
```cmake
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(std_msgs REQUIRED)
```

### Crear ejecutables
```cmake
add_executable(siro_node_suscriptor src/siro_node_suscriptor.cpp)
add_executable(siro_node_publicador src/siro_node_publicador.cpp)
```

### Vincular dependencias a los ejecutables
```cmake
ament_target_dependencies(siro_node_suscriptor rclcpp std_msgs)
ament_target_dependencies(siro_node_publicador rclcpp std_msgs)
```

### Instalar ejecutables
```cmake
install(TARGETS
    siro_node_suscriptor
    siro_node_publicador
    DESTINATION lib/${PROJECT_NAME}
)
```

### Instalar directorio launch
```cmake
install(DIRECTORY
    launch
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
```

---

## Compilar y ejecutar

```bash
cd ~/siro_ws
colcon build --packages-select cpp_siro
source install/setup.bash
ros2 run cpp_siro siro_node_publicador
```

---

## Directorios del paquete

| Directorio | Descripcion |
|------------|-------------|
| `src/` | Codigo fuente C++ (.cpp) de los nodos |
| `include/` | Headers (.hpp) para bibliotecas compartidas |
| `launch/` | Archivos de lanzamiento para iniciar multiples nodos |
| `config/` | Archivos YAML con parametros de configuracion |
| `urdf/` | Modelos URDF/Xacro del robot |
| `test/` | Pruebas automatizadas |

---

### [`↩️ Volver a paquetes`](../README.md) | [`↩️ Inicio`](../../README.md)
