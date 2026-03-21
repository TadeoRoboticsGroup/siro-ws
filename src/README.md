# Paquetes en ROS 2

En ROS 2, los paquetes organizan el codigo en unidades reutilizables. Se crean con **ament_cmake** (C++) o **ament_python** (Python).

<div align="center">
    <img src="/images/packages.png" alt="Paquetes" width="200px" max-width="800px">
</div>

<div align="center">
    <img src="/images/package_structure.svg" alt="Estructura de paquetes" width="80%" max-width="100%">
</div>

### [`↩️ Volver al inicio`](../README.md)

---

## Crear un workspace

```bash
mkdir -p ~/siro_ws/src
cd ~/siro_ws
colcon build
source install/setup.bash
```
> Ejecutar `colcon build` y `source install/setup.bash` cada vez que se haga un cambio.

Al compilar se crean 3 directorios:
```
siro_ws/
  ├── build/      # Archivos de compilacion
  ├── install/    # Paquetes instalados
  ├── log/        # Logs de compilacion
  └── src/        # Codigo fuente (tus paquetes)
```

---

## Paquetes con C++ (ament_cmake)

### Crear paquete
```bash
cd ~/siro_ws/src
ros2 pkg create --build-type ament_cmake --node-name mi_nodo mi_paquete_cpp
```

### Compilar y ejecutar
```bash
cd ~/siro_ws
colcon build --packages-select mi_paquete_cpp
source install/setup.bash
ros2 run mi_paquete_cpp mi_nodo
```

### Archivos principales

| Archivo | Funcion |
|---------|---------|
| `package.xml` | Nombre, version, dependencias y licencia del paquete |
| `CMakeLists.txt` | Configuracion de compilacion, ejecutables y dependencias |
| `src/` | Codigo fuente (.cpp) |
| `include/` | Headers (.hpp) |
| `launch/` | Archivos de lanzamiento (.py) |
| `config/` | Archivos de configuracion (.yaml) |

### [`👉 Ver paquete C++ de ejemplo`](./cpp_siro/)

---

## Paquetes con Python (ament_python)

### Crear paquete
```bash
cd ~/siro_ws/src
ros2 pkg create --build-type ament_python --node-name mi_nodo mi_paquete_py
```

### Compilar y ejecutar
```bash
cd ~/siro_ws
colcon build --packages-select mi_paquete_py
source install/setup.bash
ros2 run mi_paquete_py mi_nodo
```

### Archivos principales

| Archivo | Funcion |
|---------|---------|
| `package.xml` | Nombre, version, dependencias y licencia del paquete |
| `setup.py` | Configuracion del paquete Python (nombre, entry points) |
| `setup.cfg` | Directorio de instalacion de scripts |
| `mi_paquete_py/` | Modulo Python con `__init__.py` y nodos |
| `launch/` | Archivos de lanzamiento (.py) |
| `config/` | Archivos de configuracion (.yaml) |

> Los paquetes Python no necesitan compilarse, pero `colcon build` los instala en el workspace.

### [`👉 Ver paquete Python de ejemplo`](./python_siro/)

---

### [`↩️ Volver al inicio`](../README.md)
