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

# import streamlit as st

print("Saludador")
print("Hola inmundo!")

nombre = input("Cuál es tu nombre?")
print("Hola", nombre)

anio_nacimiento = input("En qué año naciste?")
edad = 2024 - int(anio_nacimiento)
print("Wow", nombre, "tenés como", edad, "años!")
print("Wow " + nombre + " tenés como " + str(edad) + " años!")

if edad >= 18:
    print("Igual, eso importa un pito")
    if edad >= 30:
        print("Más a esta altura")
else:
    print("Igual, eso importa poco")

# Analizar si la edad es verosímil
sospechoso = edad > 100
if sospechoso:
    print("Mmmh, dudo que seas tan viejo")

# Ingresar cantidad de veces
veces = input("Cuántas veces te lo tengo que repetir?")
# Imprimir el mensaje esa cantidad de veces
i = 0
while i < int(veces):
    print("Vos podés, " + nombre + "!")
    i = i + 1
# Ahora usando un for
for i in range(int(veces)):  # Reutilizamos la variable i
    print("Dale que podés, " + nombre + "!")
