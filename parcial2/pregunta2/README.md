# Calculadora de Expresiones Aritméticas
Calculadora de expresiones aritméticas sobre enteros que puede manejar tanto expresiones en orden pre-fijo como post-fijo.

## Características
### Operadores Soportados:

- Suma: Representada por el símbolo +.
- Resta: Representada por el símbolo -.
- Multiplicación: Representada por el símbolo *.
- División entera: Representada por el símbolo /.

### Acciones Disponibles:

- `EVAL <orden> <expr>`:

    Representa una evaluación de la expresión `<expr>` de acuerdo con el orden especificado (`<orden>`).
    `<orden>` puede ser "PRE" para expresiones en orden pre-fijo o "POST" para expresiones en orden post-fijo.
    
    #### Ejemplos:
    1. ```console
       foo@bar:~$ EVAL PRE + * + 3 4 5 7
       42
       ```
    2. ```console
       foo@bar:~$ EVAL POST 8 3 - 8 4 4 + * +
       69
       ```

- `MOSTRAR <orden> <expr>`:

    Representa una impresión en orden in-fijo de la expresión `<expr>` de acuerdo con el orden especificado (`<orden>`).
    La expresión resultante sigue las reglas de precedencia y asociatividad estándar.
    
    #### Ejemplos:
    1. ```console
       foo@bar:~$ MOSTRAR PRE + * + 3 4 5 7
       (3 + 4) * 5 + 7
       ```
    2. ```console
       foo@bar:~$ MOSTRAR POST 8 3 - 8 4 4 + * +
       8 - 3 + 8 * (4 + 4)
       ```

- `SALIR`:

    Permite salir del programa.

### Reglas de Precedencia y Asociatividad
- La suma y la resta tienen la misma precedencia.
- La multiplicación y la división entera tienen la misma precedencia.
- La multiplicación y la división entera tienen mayor precedencia que la suma y la resta.
- Todos los operadores asocian a izquierda.

## Uso
Clona este repositorio:

```bash
git clone git@github.com:thebug-code/CI3641-SD2023-Entregas.git
```
Navega al directorio del proyecto:

```bash
cd CI3641-SD2023-Entregas/tree/main/parcial2/pregunta2
```

Crea y activa un entorno virtual:

```bash
python -m venv venv
source venv/bin/activate  # Para sistemas basados en Unix/Linux
```
Instala las dependencias:

```bash
pip install -r requirements.txt
```

Ejecuta el programa:

```bash
python postfix_prefix_evaluator.py
```

Para ejecutar la prueba de cobertura, utiliza el siguiente comando:

```bash
coverage run -m unittest test_evaluator
```

Para ver el reporte de cobertura en la consola, ejecuta:

```bash
coverage report
```
