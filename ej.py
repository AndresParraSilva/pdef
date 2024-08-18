import streamlit as st
import random


state = st.session_state
if "lista1" not in state:
    state["lista1"] = []
    state["lista2"] = []

c1, c2 = st.columns(2)
with c1:
    if st.button("Agregar valor a lista 1"):
        state.lista1.append(random.randint(0, 100))
    if state.lista1:
        st.write(state.lista1)
with c2:
    if st.button("Agregar valor a lista 2"):
        state.lista2.append(random.randint(0, 100))
    if state.lista2:
        st.write(state.lista2)

if st.button("Restar lista 1 de lista 2 con tope"):
    limite = max(len(state.lista1), len(state.lista2))
    resultado = []
    for i in range(limite):
        if (
            i < len(state.lista1)
            and i < len(state.lista2)
            and state.lista2[i] > state.lista1[i]
        ):
            resultado.append(state.lista2[i] - state.lista1[i])
        else:
            resultado.append(0)
    st.write("Resultado:", resultado)
