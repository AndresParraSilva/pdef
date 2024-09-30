"""
Ejercicios con diccionarios.
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


def texto_a_dict(texto):
    caracteres = {}
    for caracter in texto:
        if caracter in caracteres:
            caracteres[caracter] += 1
        else:
            caracteres[caracter] = 1
    return caracteres


state = st.session_state
if "lista1" not in state:
    state.lista1 = []
    state.lista2 = []

st.header("Ejercicios con diccionarios")

texto_ingresado = st.text_input("Texto a analizar")
if st.button("Analizar"):
    caracteres = texto_a_dict(texto_ingresado)
    st.write(caracteres)
    st.bar_chart(caracteres, horizontal=True)  # , x=list(caracteres.keys()))
