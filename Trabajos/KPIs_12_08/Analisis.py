import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard Challenge - Ventas", layout="wide")

st.title("Dashboard de Control de Ventas")
st.caption("Herramienta analitica enfocada en la optimizacion comercial y toma de decisiones.")

@st.cache_data
def load_data():
    try:
       df = pd.read_csv("ventas.csv")
       df["Fecha"] = pd.to_datetime(df["Fecha"])
       return df
    except FileNotFoundError:
       st.error("No se encontro ´ventas.csv´. Verificar que se encuentre en la misma carpeta")
       return None
df = load_data()
if df is not None:
    st.sidebar.header("Filtros de operación")
    regiones = df["Region"].unique().tolist()
    regiones_sel = st.sidebar.multiselect("Filtrar por Región:", regiones, default=regiones)
    
    vendedores = df["Vendedor"].unique().tolist()
    vendedores_sel = st.sidebar.multiselect("Filtrar por vendedor:", vendedores, default=vendedores)

    df_filtrado = df[(df["Region"].isin(regiones_sel)) & (df["Vendedor"].isin(vendedores_sel))]

    # AL MENOS 3 KPIs
    st.markdown("Indicadores Clave de Rendimiento")
    kpi_ingresos, kpi_volumen, kpi_precio_prom = st.columns(3)
    total_ventas = df_filtrado["Ventas"].sum()
    total_unidades = df_filtrado["Cantidad"].sum()
    precio_medio = df_filtrado["Precio"].mean() if len(df_filtrado) > 0 else 0

    with kpi_ingresos:
        st.metric(label="Ingresos Totales", value=f"${total_ventas:,.2f}")
    with kpi_volumen:
        st.metric(label="Volumen Vendido (Unidades)", value=f"{total_unidades:,}")
    with kpi_precio_prom:
        st.metric(label="Precio Unitario Promedio", value=f"${precio_medio:,.2f}")

st.markdown("---")
    # Visualisacion Requerida.
col_comp, col_tend = st.columns(2)

with col_comp:
    st.subheader("⚔️ Visualización de Comparación")
    df_productos = df_filtrado.groupby("Producto")["Ventas"].sum().reset_index()
    df_productos = df_productos.sort_values(by="Ventas", ascending=False)
    
    fig_comp = px.bar(
        df_productos, 
        x="Producto", 
        y="Ventas", 
        title="Ingresos Totales por Tipo de Producto",
        labels={"Ventas": "Ventas ($)", "Producto": "Producto"},
        color="Producto",
        text_auto=".2s"
    )
    st.plotly_chart(fig_comp, use_container_width=True)

with col_tend:
    st.subheader("📉 Visualización de Tendencia")
    df_tiempo = df_filtrado.groupby("Fecha")["Ventas"].sum().reset_index()
    
    fig_tend = px.line(
        df_tiempo, 
        x="Fecha", 
        y="Ventas", 
        title="Evolución Histórica Diaria de Ventas",
        labels={"Ventas": "Monto Vendido ($)", "Fecha": "Línea de Tiempo"},
        markers=True
    )
    st.plotly_chart(fig_tend, use_container_width=True)

with col_tend:
    st.subheader("Visualización de Tendencia")
    df_tiempo = df_filtrado.groupby("Fecha")["Ventas"].sum().reset_index()
        
    fig_tend = px.line(
        df_tiempo, 
        x="Fecha", 
        y="Ventas", 
        title="Evolución Histórica Diaria de Ventas",
        labels={"Ventas": "Monto Vendido ($)", "Fecha": "Línea de Tiempo"},
        markers=True
    )
    st.plotly_chart(fig_tend, use_container_width=True) 
col_ev1, col_ev2 = st.columns(2)       
with col_ev1:
    df_region = df_filtrado.groupby("Region")["Ventas"].sum().reset_index()
    fig_pie = px.pie(
        df_region, 
        values="Ventas", 
        names="Region", 
        title="Participación de Mercado por Región",
        hole=0.4
    )
    st.plotly_chart(fig_pie, use_container_width=True)
        
with col_ev2:
# Eficiencia por Vendedor
    df_vendedor = df_filtrado.groupby("Vendedor")["Ventas"].sum().reset_index().sort_values(by="Ventas", ascending=True)
    fig_vend = px.bar(
        df_vendedor, 
        y="Vendedor", 
        x="Ventas", 
        orientation="h",
        title="Ranking de Desempeño de Vendedores",
        text_auto=".2s"
    )
    st.plotly_chart(fig_vend, use_container_width=True)

    st.markdown("---")

    # 5. ACCIONABLE Y TOMA DE DECISIONES
    st.markdown("Sección de Análisis Estratégico y Decisiones")
    
    col_insight, col_recom = st.columns(2)
    producto_top = df_productos['Producto'].iloc[0] if not df_productos.empty else "N/A"
    vendedor_top = df_vendedor['Vendedor'].iloc[-1] if not df_vendedor.empty else "N/A"
    
with col_insight:
        st.info(f"Insight Relevante Encontrado\n"
                f"Al analizar los datos filtrados, se identifica que el producto de mayor impacto comercial "
                f"actualmente es el *{producto_top}*. Adicionalmente, el asesor comercial con mayor "
                f"rendimiento acumulado es *{vendedor_top}*.\n\n"
                f"*Nota: Las métricas de tendencia muestran picos específicos de demanda que deben ser "
                f"respaldados con stock preventivo.*")

with col_recom:
        st.success("Recomendación Operativa (Para Ganar el Challenge)\n"
                   "Estrategia de Inventario: Priorizar el reabastecimiento logístico hacia las regiones de alta tracción, garantizando disponibilidad inmediata del producto líder.\n"
                   "Capacitación Comercial: Replicar las mejores prácticas y técnicas de cierre aplicadas por el vendedor estrella hacia el resto del equipo comercial para estandarizar el ticket promedio.\n"
                   "Campañas Focalizadas: Desarrollar promociones específicas cruzando datos en los días identificados con menor volumen en la gráfica de tendencia."
                   )