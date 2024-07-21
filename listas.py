"""
Creación de una lista e implementación de un algoritmo paso a paso para determinar su mayor valor
"""

import streamlit as st
import random

state = st.session_state
if "lista" not in state:
    state["lista"] = []

if st.button("Agregar valor"):
    state.lista.append(random.randint(0, 100))

if state.lista:
    st.write("Lista:", state.lista)
else:
    st.write("Lista vacía")

if st.button("Determinar mayor valor"):
    # a. definir una variable max_valor con valor inicial 0
    max_valor = 0
    # b. recorrer en un bucle los elementos de la lista
    for i in range(len(state.lista)):
        # c. para cada elemento, compararlo con max_valor
        if state.lista[i] > max_valor:
            # d. si es mayor, asignarle ese valor a max_valor
            max_valor = state.lista[i]
    # e. al terminar el bucle, imprimir max_valor
    st.write("El mayor valor de la lista es", max_valor)

if st.button("Determinar mayor valor por pares de state.lista"):
    # 1. definir max_valor con valor inicial 0
    # 2. recorrer la lista hasta el penúltimo elemento
    # 3. sumar el elemento actual y el próximo
    # 4. compararlo con max_valor
    # 5. Si es mayor, asignar el nuevo valor a max_valor
    # 6. Imprimir el mayor valor por pares de la lista

    # 1. Definir max_valor con valor inicial 0
    max_valor = 0
    
    # 2. Recorrer la lista hasta el penúltimo elemento
    for i in range(len(state.lista) - 1):
        # 3. Sumar el elemento actual y el próximo
        suma_pares = state.lista[i] + state.lista[i + 1]
        
        # 4. Compararlo con max_valor
        if suma_pares > max_valor:
            # 5. Si es mayor, asignar el nuevo valor a max_valor
            max_valor = suma_pares
    
    # 6. Imprimir el mayor valor por pares de la lista
    st.write("El mayor valor por pares de la lista es", max_valor)
