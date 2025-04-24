# Backend de la Aplicación Dockerizada

Este repositorio contiene el backend de la aplicación, que está dockerizado para facilitar su configuración y despliegue.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente en tu máquina:

- [Docker](https://www.docker.com/get-started) (para ejecutar contenedores)
- [Docker Compose](https://docs.docker.com/compose/install/) (opcional, para orquestar múltiples contenedores, si es necesario)

### 1. Clonar el Repositorio

Clona este repositorio a tu máquina local:

```bash
git clone <url_del_repositorio>
cd <nombre_del_repositorio>

### 2. Construir la Imagen de Docker

Dentro del directorio del proyecto, construye la imagen de Docker usando el siguiente comando:

```bash
docker build -t backend-app .

### 3. Ejecutar el Contenedor

Para ejecutar el contenedor y poner en marcha el backend, usa el siguiente comando:

```bash
docker run -p 5000:5000 backend-app

### 4. Verificar el Funcionamiento

Abre tu navegador y visita:

http://localhost:5000
