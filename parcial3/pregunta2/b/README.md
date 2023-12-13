# Conteo de archivos en subdirectorios
Programa en C que dado un path que representa un directorio en el sistema operativo, cuenta la cantidad de archivos ubicados en el subárbol que tiene como raíz el directorio propuesto. El proceso está diseñado para crear un hilo por cada subdirectorio encontrado.

## Instalación:

1. Clonar el repositorio:
    ```bash
    git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
    ```
2. Navega al directorio del proyecto:
    ```
    cd CI3641-SD2023-Entregas/parcial3/pregunta2/b
    ```

3. Compilar el programa:
    ```bash
    make
    ```

## Uso

Después de compilar el programa correctamente, puedes ejecutarlo con el siguiente comando:
```bash
./countfiles <path>
```
Sustituye `<path>` con el directorio raíz del cual deseas contar la cantidad de archivos en el subárbol.

