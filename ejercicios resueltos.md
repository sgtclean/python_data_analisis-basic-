Parte 1 - Análisis básico 

El programa calcula lo siguiente a partir del archivo `ventas.csv`:

- ✅ Número total de ventas registradas
- ✅ Número de productos únicos vendidos
- ✅ Ingreso total (precio × cantidad por venta)
- ✅ Producto más vendido
- ✅ Ventas totales por país

Los resultados se guardan automáticamente en un archivo llamado `ventas.txt`.

---

Parte 2 - Visualización con matplotlib y seaborn

El script genera varios gráficos para comprender mejor los datos:

1. **Top 5 productos más vendidos**  
   Gráfico de barras ordenado por cantidad total vendida.

2. **Distribución de precios**  
   Histograma que muestra cuántas veces aparece cada rango de precios.

3. **Ventas por categoría**  
   Gráfico de barras con las cantidades vendidas por categoría.

4. **Boxplot: precio por categoría**  
   Muestra la dispersión y distribución de los precios según la categoría del producto.

> Todos los gráficos se muestran con `plt.show()` y pueden guardarse si se desea en una carpeta `/graficos`.

---

Parte 3 - Análisis avanzado


- ¿Qué país genera más ingresos?
- ¿Qué categoría tiene mayor ingreso promedio por venta?
- ¿Existe relación entre precio y cantidad vendida?
- ¿Qué día de la semana se vende más?

> Estas preguntas están planteadas en el script y listas para ser resueltas como ejercicios de práctica avanzada.

