# Calculadora de Expresiones Aritméticas
Calculadora de expresiones aritméticas sobre enteros que puede manejar tanto expresiones en orden pre-fijo como post-fijo.

## Características
### Operadores Soportados:

- Suma: Representada por el símbolo +.
- Resta: Representada por el símbolo -.
- Multiplicación: Representada por el símbolo *.
- División entera: Representada por el símbolo /.

### Acciones Disponibles:

- EVAL <orden> <expr>:

Representa una evaluación de la expresión en <expr> de acuerdo con el orden especificado (<orden>).
<orden> puede ser "PRE" para expresiones en orden pre-fijo o "POST" para expresiones en orden post-fijo.

#### Ejemplos:
1. EVAL PRE + * + 3 4 5 7 deberá imprimir 42.
2. EVAL POST 8 3 - 8 4 4 + * + deberá imprimir 69.

- MOSTRAR <orden> <expr>:

Representa una impresión en orden in-fijo de la expresión en <expr> de acuerdo con el orden especificado (<orden>).
La expresión resultante sigue las reglas de precedencia y asociatividad estándar.

#### Ejemplos:
1. MOSTRAR PRE + * + 3 4 5 7 deberá imprimir (3 + 4) * 5 + 7.
2. MOSTRAR POST 8 3 - 8 4 4 + * + deberá imprimir 8 - 3 + 8 * (4 + 4).

- SALIR:

Permite salir del programa.

### Reglas de Precedencia y Asociatividad
- La suma y la resta tienen la misma precedencia.
- La multiplicación y la división entera tienen la misma precedencia.
- La multiplicación y la división entera tienen mayor precedencia que la suma y la resta.
- Todos los operadores asocian a izquierda.

## Uso
Clona este repositorio:

```
git clone https://github.com/tu-usuario/calculadora-expresiones.git
```
Navega al directorio del proyecto:

```
cd calculadora-expresiones
```

Crea y activa un entorno virtual:

```
python -m venv venv
source venv/bin/activate  # Para sistemas basados en Unix/Linux
```
Instala las dependencias:

```
pip install -r requirements.txt
```

Ejecuta el programa:

```
python calculadora.py
```

Para ejecutar la prueba de cobertura, utiliza el siguiente comando:

```
coverage run -m unittest test_evaluator
```

Para ver el reporte de cobertura en la consola, ejecuta:

```
coverage report
```

