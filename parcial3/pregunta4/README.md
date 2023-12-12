# Manejador de Tablas de Métodos Virtuales
Este proyecto implementa un manejador de tablas de métodos virtuales para un sistema orientado a objetos con herencia simple y despacho dinámico de métodos en Python.

## Instalacion :rocket:

1. Clona el repositorio:

    ```bash
    git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd CI3641-SD2023-Entregas/parcial3/pregunta4
    ```

3. Instala las dependencias 

    ```bash
    pip install -r requirements.txt
    ```

## Uso :video_game:

Una vez instaladas las dependencias, puedes ejecutar el programa interactivo. El programa solicitará al usuario realizar acciones, que incluyen la definición de clases, descripción de tablas de métodos virtuales y salir del simulador.

Ejemplos:

- **Definir una nueva clase:**
    ```bash
    CLASS A f g
    ```

- **Definir una clase con herencia:**
    ```bash
    CLASS B : A f h
    ```

- **Describir la tabla de métodos de una clase:**
    ```bash
    DESCRIBIR B
    ```

- **Salir del simulador:**
    ```bash
    SALIR
    ```

## Ejecutar Pruebas con Cobertura

El proyecto incluye un conjunto de pruebas para verificar el correcto funcionamiento del manejador. Para ejecutarlas, use el siguiente comando:
    ```bash
    coverage run -m test_vtable
    ```

Para generar un reporte de cobertura, ejecute el siguiente comando:
    ```bash
    coverage report -m
    ```

