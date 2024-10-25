import streamlit as st
import pandas as pd
import plotly.express as px

# Función para cargar datos desde un archivo CSV
def cargar_datos():
    try:
        return pd.read_csv('data/ventas.csv')  # Asegúrate de que la ruta sea correcta
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()  # Devuelve un DataFrame vacío en caso de error


# Título del dashboard
st.title("Dashboard de Análisis de Ventas")

# Describe dashboard
st.write("Este dashboard permite analizar las ventas por categoría y producto.")

# Cargar datos desde ventas.csv
df = cargar_datos()

# Filtros 
categorias = df['categoria'].unique()  # Obtener las categorías únicas
categoria_seleccionada = st.selectbox("Selecciona una categoría", categorias)  # Dropdown para seleccionar categoría

# Filtramos por la categoría seleccionada
df_filtrado = df[df['categoria'] == categoria_seleccionada]

# Gráfico 1: Ventas por producto (barras)
st.subheader(f"Ventas por Producto en la Categoría {categoria_seleccionada}")
fig1 = px.bar(df_filtrado, x='producto', y='ventas', title=f'Ventas por Producto en {categoria_seleccionada}')
st.plotly_chart(fig1)  # Mostrar gráfico en el dashboard

# Gráfico 2: Evolución de ventas a lo largo del tiempo (línea)
st.subheader(f"Evolución de Ventas en {categoria_seleccionada}")
fig2 = px.line(df_filtrado, x='fecha', y='ventas', title=f'Evolución de Ventas en {categoria_seleccionada}', markers=True)
st.plotly_chart(fig2)  # Mostrar gráfico en el dashboard

# Gráfico 3: Distribución de ventas (pastel)
st.subheader(f"Distribución de Ventas por Producto en {categoria_seleccionada}")
fig3 = px.pie(df_filtrado, names='producto', values='ventas', title=f'Distribución de Ventas por Producto en {categoria_seleccionada}')
st.plotly_chart(fig3)  # Mostrar gráfico de pastel

# Mostrar tabla de datos filtrados
st.write("Datos filtrados por la categoría seleccionada:")
st.dataframe(df_filtrado)  # Mostrar la tabla con los datos filtrados

# Mostrar resumen estadístico de las ventas
st.subheader("Resumen Estadístico de las Ventas")
st.write(df_filtrado.describe())

