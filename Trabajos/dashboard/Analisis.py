import streamlit as st
import pandas as pd
import plotly.express as px

# Configuracion del dashboard
st.set_page_config(page_title="Dashboard de Ventas", layout="wide")
st.title("Analisis de Desempeño del Negocio")
# 1.- Cargar datos.
@st.cache_data
def cargar_datos():
    df = pd.read_csv("Trabajos/dashboard/ventas.csv")
    if "Fecha" in df.columns:
        df["Fecha"] = pd.to_datetime(df["Fecha"])
    return df

df = cargar_datos()

# Pregunta 1: ¿Como esta funcionando el negocio?
st.header("Rendimiento general del negocio")
col1, col2 = st.columns(2)
with col1:
    total_ingresos = df["Ventas"].sum()
    st.metric(label="Ingresos Totales", value=f"${total_ingresos:,.2f}")
with col2:
    total_unidades = df["Cantidad"].sum() 
    st.metric(label="Total unidades o transacciones", value=f"{total_unidades}")

# Pregunta 2: ¿Que producto vende mas?
st.header("Producto mas vendido")
ventas_producto = df.groupby("Producto")["Ventas"].sum().reset_index()
ventas_producto = ventas_producto.sort_values(by="Ventas", ascending=False)
fig_prod = px.bar(ventas_producto.head(10), x ="Producto", y="Ventas", title="Top 10 productos por ingreso")
st.plotly_chart(fig_prod, use_container_width=True)

# Pregunta 3: ¿Que region tiene mejor desempeño?
st.header("Desempeño por Región")
if "Region" in df.columns:
    ventas_region = df.groupby("Region")["Ventas"].sum().reset_index()
    fig_reg = px.pie(ventas_region, values="Ventas", names="Region", title="Distribución de Ventas por Región")
    st.plotly_chart(fig_reg, use_container_width=True)
else:
    st.warning("No se encontro una columna region en el archivo.")

# Pregunta 4: ¿Existe alguna tendencia preocupante?
st.header("Tendencias Temporales (Línea de Tiempo)")
if "Fecha" in df.columns:
    df["Mes"] = df["Fecha"].dt.to_period("M").astype(str)
    ventas_tiempo = df.groupby("Mes")["Ventas"].sum().reset_index()
    fig_line = px.line(ventas_tiempo, x="Mes", y="Ventas", title="Evolución de Ventas Mensuales")
    st.plotly_chart(fig_line, use_container_width=True)

else:
    st.warning("No se encontró una columna ´Fecha´ para analizar tendencias.")

# Pregunta 5: Recomendaciones.
st.header("Acciones Recomendadas")
st.write("- **Focalización**: Reforzar el marketing en los productos menos vendidos o empujar el inventario del producto estrella.")
st.write("- **Atención**: Si la tendencia temporal va a la baja, revisar las estrategias de precios o competencia.")