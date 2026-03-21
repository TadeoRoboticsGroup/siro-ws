# Instalacion de ROS 2 Humble

Para instalar ROS 2 en tu sistema utilizando paquetes Debian. Estas instrucciones asumen Ubuntu 22.04 LTS o superior con privilegios de superusuario.

<div align="center">
    <img src="/images/install_flow_diagram.svg" alt="Flujo de instalacion" width="80%" max-width="100%">
</div>

### [`↩️ Volver al inicio`](./README.md)

---

## Instalacion con paquetes Debian

> **Requisito**: Ubuntu 22.04 LTS o versiones LTS superiores.

### Configuracion de fuentes

1. Configuracion regional compatible con UTF-8.
```bash
locale  # check for UTF-8

sudo apt update && sudo apt install locales
sudo locale-gen en_US en_US.UTF-8
sudo update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8
export LANG=en_US.UTF-8

locale  # verify settings
```

2. Habilitar el repositorio Ubuntu Universe.
```bash
sudo apt install software-properties-common
sudo add-apt-repository universe
```

3. Agregar la clave GPG de ROS 2.
```bash
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
```

4. Agregar el repositorio a la lista de fuentes.
```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
```

### Instalar paquetes de ROS 2

5. Actualizar cache y sistema.
```bash
sudo apt update && sudo apt upgrade
```

6. Instalar ROS 2.

> **Version Desktop** (recomendada): Incluye RVIZ2, ejemplos y tutoriales.
```bash
sudo apt install ros-humble-desktop
```

> **Version Base**: Solo bibliotecas de comunicacion, mensajes y herramientas CLI.
```bash
sudo apt install ros-humble-ros-base
```

7. Herramientas de desarrollo.
```bash
sudo apt install ros-dev-tools
```

8. Herramienta de compilacion de workspaces.
```bash
sudo apt install python3-colcon-common-extensions
```

---

## Verificar la instalacion

1. Cargar el entorno de ROS 2.
```bash
source /opt/ros/humble/setup.bash
```

2. En una terminal, ejecutar el nodo publicador de prueba.
```bash
ros2 run demo_nodes_cpp talker
```

3. En otra terminal, ejecutar el nodo suscriptor de prueba.
```bash
source /opt/ros/humble/setup.bash
ros2 run demo_nodes_cpp listener
```

> Si ves mensajes como `[INFO] [talker]: Publishing: 'Hello World: 1'` y `[INFO] [listener]: I heard: [Hello World: 1]`, la instalacion fue exitosa.

---

## Configuracion recomendada

Cargar ROS 2 automaticamente al abrir cada terminal:
```bash
echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc
```

---

### [`↩️ Volver al inicio`](./README.md)
