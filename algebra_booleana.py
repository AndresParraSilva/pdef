"""
Ejercicios de álgebra booleana con dos listas de igual tamaño.
"""

import streamlit as st
import random


def ambos_pares(lis1, lis2):
    """Suma si ambos son pares, resta si no."""
    res = []
    for i in range(len(lis1)):
        if lis1[i] % 2 == 0 and lis2[i] % 2 == 0:
            res.append(lis1[i] + lis2[i])
        else:
            res.append(lis1[i] - lis2[i])
    return res


def solo_uno(lis1, lis2):
    res = []
    for i in range(len(lis1)):
        if (lis1[i] % 2 == 0) ^ (lis2[i] % 2 == 0):
            res.append(lis1[i] + lis2[i])
        else:
            res.append(lis1[i] - lis2[i])
    return res


state = st.session_state
if "lista1" not in state:
    state.lista1 = []
    state.lista2 = []

st.header("Álgebra booleana")

c1, c2 = st.columns(2)
with c1:
    if st.button("Agregar valor lista1"):
        state.lista1.append(random.randint(0, 100))
    if state.lista1:
        st.write("Lista:", state.lista1)
    else:
        st.write("Lista vacía")
with c2:
    if st.button("Agregar valor lista2"):
        state.lista2.append(random.randint(0, 100))
    if state.lista2:
        st.write("Lista:", state.lista2)
    else:
        st.write("Lista vacía")

if len(state.lista1) > 0 and len(state.lista1) == len(state.lista2):
    if st.button("Ambos pares (AND)"):
        resultado = ambos_pares(state.lista1, state.lista2)
        st.write(resultado)

    if st.button("Solo uno (XOR)"):
        resultado = solo_uno(state.lista1, state.lista2)
        st.write(resultado)
