# Producto punto entre dos arreglos
Programa en C que dado dos argumentos pasados por la línea de comandos, digamos, `N` y `T` calcula el producto escalar entre dos vectores generados aleatoriamente de `N` elementos enteros cada uno. El cálculo se realiza usando `T` hilos; cada hilo calcula un producto escalar parcial y luego estos se suman para obtener el resultado final, el cual se muestra en pantalla.

## Instalación
1. Clona el repositorio:

    ```bash
    git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
    ```

2. Navega al directorio del proyecto:

    ```bash
    cd CI3641-SD2023-Entregas/parcial3/pregunta2
    ```    
3. Compilar el programa
```bash
make
```        

## Uso     
Para ejecutar el programa, utilice el siguiente comando:
```bash
./dotproduct <N> <num-threads>
```

Sustituye `<N>` por el número de elementos del arreglo y `<num-threads>` por el número de hilos que desees.
