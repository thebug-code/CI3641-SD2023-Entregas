# Producto punto entre dos arreglos
Dado dos argumentos pasados por la línea de comandos, digamos, `N` y `T`. El programa calcula el producto escalar entre dos vectores generados aleatoriamente de `N` elementos enteros cada uno. El cálculo se realiza usando `T` hilos; cada hilo calcula un producto escalar parcial y luego estos se suman para obtener el resultado final, el cual se muestra en pantalla.

## Instalación
1. Clona el repositorio:

    ```bash
    git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd CI3641-SD2023-Entregas/parcial3/pregunta2
    ```

## Uso
Una vez ubicado en el directorio, puedes compilar el programa con el siguiente comando:
```bash
make
```

Para ejecutar el programa, utilice el siguiente comando:
```bash
./dotproduct <N> <num-threads>
```

Donde `N` es el número de elementos del arreglo y `num-threads` es el número de hilos para el calculo del producto.
