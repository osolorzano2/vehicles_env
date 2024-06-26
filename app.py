import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Datos de odómetros en venta de vehiculos')

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos
hist_button = st.checkbox('Construir histograma')  # crear un botón
disp_button = st.checkbox('Construir grafico de dispersion')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

if disp_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write(
        'Grafico de dispersion para el conjunto de datos de anuncios de venta de coches')

    # crear un scatter
    fig = px.scatter(car_data, x="odometer", y="price")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
