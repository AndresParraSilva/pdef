"""
Clásico programa "Hola mundo", con revisión de:
* Impresión en pantalla
* Variables
* Ingreso de datos
* Operaciones matemáticas y de cadenas de texto
* Tipos de datos
* Condicionales
* Comentarios
* Bucles
"""

import streamlit as st

st.title("Saludador")
st.write("Hola inmundo!")

nombre = st.text_input("Cuál es tu nombre?")
st.write("Hola", nombre)

anio_nacimiento = st.text_input("En qué año naciste?")
edad = 2024 - int(anio_nacimiento)
st.write("Wow", nombre, "tenés como", edad, "años!")
st.write("Wow " + nombre + " tenés como " + str(edad) + " años!")

if edad >= 18:
    st.write("Igual, eso importa un pito")
    if edad >= 30:
        st.write("Más a esta altura")
else:
    st.write("Igual, eso importa poco")

# Analizar si la edad es verosímil
sospechoso = edad > 100
if sospechoso:
    st.write("Mmmh, dudo que seas tan viejo")

# Ingresar cantidad de veces
veces = st.text_input("Cuántas veces te lo tengo que repetir?")
# Imprimir el mensaje esa cantidad de veces
i = 0
while i < int(veces):
    st.write("Vos podés, " + nombre + "!")
    i = i + 1
# Ahora usando un for
for i in range(int(veces)):  # Reutilizamos la variable i
    st.write("Dale que podés, " + nombre + "!")
