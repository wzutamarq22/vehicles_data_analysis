import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

# Leer el dataset
df = pd.read_csv('vehicles_us.csv')

# Crear la columna 'brand' con la primera palabra (la marca)
df['brand'] = df['model'].str.split().str[0]

# Crear la columna 'model' con todo lo que viene después de la marca
df['model'] = df['model'].str.split(n=1).str[1]

# Encabezado de la aplicación
st.header(
    "Análisis Exploratorio de Datos de las Ventas de Vehículos Nuevos y Usados en EE.UU.")

# Botón para construir un histograma
if st.button("Construir Histograma"):
    st.write("Histograma de la columna 'odometer'")
    if 'odometer' in df.columns:
        fig = px.histogram(df, x='odometer', title='Histograma de Odómetro')
    else:
        fig = px.histogram(
            df, x=df.columns[0], title=f'Histograma de {df.columns[0]}')
    st.plotly_chart(fig, use_container_width=True)

# Gráfico de dispersión con selección de marca
st.subheader(
    "Gráfico de Dispersión segun Condicion de Vehiculos: Precio vs Odómetro por Marca")

brand_list = ['todas']
brand_list.extend(df['brand'].unique().tolist())
df_scatter = df[df['brand'].isin(brand_list)]
df_scatter_2 = df_scatter.groupby(['brand', 'condition']).agg(
    {'odometer': 'mean', 'price': 'mean'}).reset_index()
# fig_scatter = px.scatter(df_scatter_2, x="odometer", y="price", color="brand")#
#                 #size='petal_length', hover_data=['petal_width'])
# fig_scatter.show()

marca_seleccionada = st.multiselect(
    "Selecciona una marca:", brand_list)
if marca_seleccionada != 'todas':
    df_filtered = df_scatter_2[df_scatter_2['brand'].isin(marca_seleccionada)]
    fig_filtered = px.scatter(df_filtered, x="odometer", y="price", color="condition",
                              title=f"Precio vs Odómetro para {marca_seleccionada}")
    st.plotly_chart(fig_filtered, use_container_width=True)
else:
    fig_filtered = px.scatter(df_scatter_2, x="odometer", y="price", color="condition",
                              title=f"Precio vs Odómetro para {marca_seleccionada}")
    st.plotly_chart(fig_filtered, use_container_width=True)
