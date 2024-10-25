import pandas as pd
import streamlit as st
import plotly.express as px 

def cargar_datos():
    try:
        df = pd.read_csv('ventas.csv', encoding='latin1')  # Ajusta la codificación según sea necesario
        df.columns = df.columns.str.strip()  # Elimina espacios en blanco de los nombres de columnas
        st.write("Columnas disponibles:", df.columns.tolist())  # Imprime las columnas disponibles para depuración
        return df
    except Exception as e:
        st.error(f"Error al cargar los datos: {e}")
        return pd.DataFrame()

# Título del dashboard
st.title("Dashboard de Análisis de Ventas")

# Cargar los datos
df = cargar_datos()

# Verificar si el DataFrame no está vacío
if not df.empty:
    # Obtener las categorías únicas
    if 'categoria' in df.columns:  # Verifica si la columna 'categoria' existe
        categorias = df['categoria'].unique()  # Asegúrate de que esta columna exista
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
    else:
        st.error("La columna 'categoria' no existe en los datos.")
else:
    st.error("No se pudieron cargar datos para mostrar.")
