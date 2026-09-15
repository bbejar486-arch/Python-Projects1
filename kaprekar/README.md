# 🔢 Constante de Kaprekar

Programa desarrollado en **Python** que implementa el algoritmo de la **Constante de Kaprekar (6174)** para números de cuatro dígitos.

El programa toma un número ingresado por el usuario y realiza sucesivamente el proceso de Kaprekar hasta alcanzar el número **6174**.

## ⚙️ ¿Cómo funciona?

En cada iteración el programa:

1. Separa el número en sus cuatro dígitos.
2. Ordena los dígitos de forma ascendente.
3. Ordena los mismos dígitos de forma descendente.
4. Resta el número menor al número mayor.
5. Repite el proceso utilizando el resultado obtenido.
6. Finaliza cuando alcanza la constante **6174**.

Durante la ejecución se muestran los números ordenados, el resultado de cada resta y la cantidad de iteraciones realizadas.

## 🧠 Conceptos aplicados

- Listas
- Ciclos `for` y `while`
- Condicionales
- Manejo de strings
- Conversión entre `str` e `int`
- Uso de banderas
- Contadores
- Ordenamiento manual de elementos
- Resolución de problemas mediante algoritmos

## 💡 Característica del proyecto

El ordenamiento de los dígitos fue implementado manualmente mediante ciclos y comparaciones, sin utilizar funciones de ordenamiento automático de Python.

Esto permite practicar y comprender la lógica detrás de los algoritmos de ordenamiento.

## ▶️ Ejecución

Para ejecutar el programa:

```bash
python kaprekar.py
```

Luego se debe ingresar un número de cuatro dígitos.

### Ejemplo

```text
Ingrese un número de 4 dígitos: 3524

Ascendente: 2345
Descendente: 5432
Resultado: 3087

...

Se ha llegado a la constante de Kaprekar: 6174
```

## 🎯 Objetivo

Este proyecto fue desarrollado como práctica de **lógica de programación y algoritmos**, con el objetivo de reforzar el manejo de estructuras de control, listas y ordenamientos en Python.
