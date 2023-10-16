# Kotlin Vector Library

Este proyecto implementa una librería en Kotlin para trabajar con vectores tridimensionales y realizar operaciones aritméticas básicas en ellos.

## Características

El módulo cumple con las siguientes características:

- Suma de vectores: representada por el símbolo `+`.
- Resta de vectores: representada por el símbolo `-`.
- Producto cruz de vectores: representada por el símbolo `*`.
- Producto punto de vectores: representada por el símbolo `%`.
- Cálculo de la norma de un vector: representada por el símbolo `&`.

## Uso

Para utilizar y probar esta librería, debes seguir estos pasos:

1. Clona este repositorio a tu sistema local:

   ```bash
   git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git

    ```
2. Ingresa al directorio del proyecto:
    ```
    cd CI3641-SD2023-Entregas/parcial1/pregunta4
    ```
3. Compila el código utilizando el comando make:
    ```
    make
    ```
4. Ejecuta el programa de prueba `VectorTest`:
    ```
    ./runTestVector
    ```

Esto ejecutará las pruebas de la librería y mostrará los resultados.

## Prueba de Cobertura

Para realizar una prueba de cobertura en la librería, sigue estos pasos:

1. Asegúrate de haber seguido los pasos anteriores para compilar el código

2. Ejecuta el script `runCodeCov`:
   ```bash
   ./runCodeCov
   ```

Una vez que la prueba de cobertura se haya completado, puedes ver el informe en la siguiente ubicación:
```
coverage-report/com.threedimvector/Vector.html
```
