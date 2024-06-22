### Apuntes de la Tercera Clase de Programación

### 1. Concatenación de Cadenas de Texto

La concatenación es el proceso de unir dos o más cadenas de texto para formar una sola. En muchos lenguajes de programación, esto se hace utilizando el operador `+`.

Concatenar texto es una operación fundamental en la programación, habiéndose utilizado desde los primeros lenguajes de alto nivel como Fortran y COBOL. Es esencial para la creación dinámica de mensajes, generación de informes, y más.

**Ejemplo en Streamlit:**
```python
st.write("Wow " + nombre + " tenés como " + str(edad) + " años!")
```
Aquí estamos uniendo (concatenando) varias cadenas de texto y una variable numérica que primero convertimos a texto (string) usando `str()`.

**F-strings:**
Introducidas en Python 3.6, las f-strings (o formatted string literals) ofrecen una manera más sencilla y elegante de incrustar variables dentro de cadenas de texto.
```python
st.write(f"Wow {nombre} tenés como {edad} años!")
```

### 2. Operaciones “Matemáticas” sobre Cadenas de Texto

Las operaciones matemáticas como suma, resta, multiplicación y división no son aplicables a cadenas de texto de la misma manera que lo son a números, pero pueden tener comportamientos definidos en algunos lenguajes.

La manipulación de texto en operaciones aritméticas puede tener resultados inesperados. En el contexto de Python, algunas operaciones están sobrecargadas para trabajar con cadenas.

**Ejemplo en Streamlit:**
```python
st.write("Wow" + "!")
st.write("Wow" * 3)  # Repetición de la cadena tres veces
```

### 3. Operador Condicional Ternario

El operador ternario es una forma compacta de escribir una condición if-else en una sola línea.

Introducido en lenguajes como C y adoptado por muchos otros, permite una escritura más concisa de condiciones sencillas:
```python
st.write("Igual, eso importa " + ("un pito" if edad >= 18 else "poco"))
```
En Python, se escribe en la forma `X if condition else Y`.

### 4. if… elif… else…

Las sentencias `if`, `elif` y `else` permiten que un programa tome diferentes caminos de ejecución basados en condiciones lógicas.

Condicionales como `if` y `else` son pilares de la programación estructurada, una técnica popularizada por lenguajes como ALGOL y C. 

**Ejemplo en Streamlit:**
```python
if edad >= 30:
    st.write("A esta altura da igual")
elif edad >= 18:
    st.write("Igual, eso importa un pito")
else:
    st.write("Igual, eso importa poco")
```

### 5. Bucle for

El bucle `for` es una estructura de control que repite un bloque de código un número determinado de veces.

Los bucles son otra piedra angular de la programación. Originalmente implementados en lenguajes como Fortran, permiten iterar sobre colecciones y generar secuencias de manera eficiente.

**Ejemplo en Streamlit:**
```python
for i in range(int(veces)):
    st.write("Dale que podés, " + nombre + "!")
```

### 6. Uso de Python y la Consola en vez de Streamlit

Streamlit es una herramienta útil para crear aplicaciones web, pero en muchos casos, es conveniente conocer cómo ejecutar scripts directamente en la consola de Python.

Python, al ser un lenguaje interpretado, permite la ejecución interactiva de comandos lo que facilita el aprendizaje y la depuración.
```python
# En el terminal:
python holass.py
```

### 7. Sobrecarga de operadores

La sobrecarga de operadores permite definir operadores (como `+`, `*`, `-`, etc.) para que funcionen con diferentes tipos de datos de manera específica.

Este concepto viene de lenguajes como C++ donde la sobrecarga permite hacer más intuitivos ciertos tipos de operaciones entre objetos de clases definidas por el usuario.

**Ejemplo en Streamlit:**
```python
st.write("Wow" * 3)  # Esto imprime "WowWowWow"
```

### Tarea Clase 3

Experimentar con operadores en la consola de Python ayuda a comprender cómo se comportan con diferentes tipos de datos.
Ingresas con `python`.
```
Python 3.8.10 (default, Nov 22 2023, 10:22:35) 
[GCC 9.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> print(1 + 1)
2
>>>
```
Sales con `exit()`.

También recomendamos utilizar recursos en línea como CodeChef para practicar Python. Las tareas están diseñadas para reforzar la comprensión de cómo Python maneja tipos de datos y operadores. 

Cada concepto que aprendes es un paso más hacia la creación de aplicaciones impresionantes. La programación puede ser un desafío, pero con cada línea de código que escribes, te acercas a dominar un lenguaje que te permitirá transformar ideas en realidad. ¡Sigue explorando y nunca dejes de aprender! ¡Tú puedes!