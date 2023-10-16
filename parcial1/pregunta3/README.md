# Manejo de Memoria con Buddy System

Este proyecto implementa un manejador de memoria utilizando el algoritmo Buddy System. El programa es interactivo y permite reservar y liberar bloques de memoria, así como mostrar el estado de la memoria en cualquier momento.

## Características

El programa cumple con las siguientes características:

1. Recibe como argumento la cantidad de bloques de memoria que manejará.
2. Una vez iniciado el programa, el usuario puede realizar las siguientes acciones:

    - Reservar memoria: `RESERVAR <cantidad> <nombre>`
    
      Esto reserva espacio de `<cantidad>` bloques de memoria y lo asocia al identificador `<nombre>`. El programa reporta un error si `<nombre>` ya tiene memoria reservada o no hay suficiente espacio contiguo.

    - Liberar memoria: `LIBERAR <nombre>`
    
      Esto libera el espacio asociado al identificador `<nombre>`. El programa reporta un error si `<nombre>` no tiene memoria reservada.

    - Mostrar el estado de la memoria: `MOSTRAR`
    
      Muestra una representación gráfica en texto de las listas de bloques libres, así como la información de nombres y la memoria que tienen asociada.

    - Salir del simulador: `SALIR`

3. Para iniciar el programa, ejecuta el siguiente comando:
   ```bash
   python main.py <cantidad_de_bloques>
   ```

   Donde `<cantidad_de_bloques>` es el número de bloques que deseas admistrar administrar.

## Ejecución de Pruebas

Para ejecutar las pruebas unitarias, utiliza el siguiente comando:
```bash
python -m unittest test_buddy.py
```
Además, puedes medir la cobertura de las pruebas utilizando la biblioteca `coverage` de Python. Sigue estos pasos:

1. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```
2. Ejecuta las pruebas con cobertura:
    ```bash
    coverage run -m unittest test_buddy.py
    ```
3. Genera el informe de cobertura:
    ```bash
    coverage report
    ```
Esto te proporcionará información sobre la cobertura de las pruebas.
