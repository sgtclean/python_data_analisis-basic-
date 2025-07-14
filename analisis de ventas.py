import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv(r"C:\Users\Asus\OneDrive\Escritorio\py\ventas.csv")

#ventas totales
ventas_tot=len(data)


#cuantos productos unicos se vendieron
productos_unicos = data['Producto'].nunique()
#nunique obtiene el str que existe en la celda, pero, no suma los valores, solo revisa los elementos unicos

#obtenemos el ingreso total
ing_tot=(data["Precio"]*data["Cantidad"]).sum()


#producto mas vendido
new=data.groupby("Producto")["Cantidad"].sum().reset_index()
#reset index nos ayuda a no quitar los nombres de las columnas
condicion = new["Cantidad"] == new["Cantidad"].max()
#pocemos hacer una condicion para comparar filas y aislarlas en un nuevo data frame
fila_max = new[condicion]


#ventas por pais
pais=data.groupby("Pais")["Cantidad"].sum().reset_index()

# usas as f para acortar toda la operacion y usar f como el archivo para no escribir ventas.txt y ahorrar trabajo
with open ("ventas.txt", "w") as f:
    f.write("ventas totales:")
    f.write(str(ventas_tot) + "\n\n")
    f.write("productos unicos vendidos:")
    f.write(str(productos_unicos)+ "\n\n")
    f.write("ingresos totales:")
    f.write(str(ing_tot)+ "\n\n")
    f.write("productos mas vendidos:")
    f.write(str(fila_max)+ "\n\n")
    f.write("ventas por pais:")
    f.write(str(pais)+ "\n\n")


######################################################################


    #parte 2 "analisis con seaborn"

    #grafico de barras con el top 5 de cosas vendidas
top=new.sort_values(by='Cantidad', ascending=False)
#usas sort values para ordenar el data frame 
top_5=top.head(5)
sns.barplot(x="Producto", y="Cantidad", data=top_5)
print(top_5)
plt.title('top 5 productos mas vendidos')
plt.xlabel('producto')
plt.ylabel('Cantidad vendida')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()

    #histograma de distribucion de precios
precio=data.groupby("Precio")["Producto"].nunique().reset_index()
plt.hist(data["Precio"], bins=10, edgecolor="black")
plt.title('Histograma de precios')
plt.xlabel('Rango de Precios')
plt.ylabel('Cantidad de productos')
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()
    #grafico de barras de venta por categoria
categorias = data.groupby("Categoria")["Cantidad"].sum().reset_index()
sns.barplot(x='Categoria', y='Cantidad', data=categorias)
plt.title('ventas por categoria')
plt.show()


    #boxplot precio por categoria
sns.boxplot(x="Categoria", y="Precio", data=data)
plt.title("Distribución de precios por categoría")
plt.show()

    #linea de tiempo ventas por mes
data['Fecha'] = pd.to_datetime(data['Fecha'])
data["Mes"]= data["Fecha"].dt.to_period("M")
# Agrupamos por mes y sumamos ingresos

ingresos_mensuales = data.groupby("Mes").apply(lambda x: (x["Precio"] * x["Cantidad"]).sum()).reset_index(name="Ingresos")
#en este caso usamos lambda para defirnir una operacion ya que solo la utilizaremos una vez en vez de usar def

ingresos_mensuales["Mes"] = ingresos_mensuales["Mes"].astype(str)
#transformamos la fecha en elementos tipo str para que no tenga problemas con seaborn

# Graficamos
sns.lineplot(x="Mes", y="Ingresos", data=ingresos_mensuales, marker="o")
plt.title("Ingresos por mes")
plt.xlabel("Mes")
plt.ylabel("Ingreso total")
plt.grid(True)
plt.tight_layout()
plt.show()


#######################################################################

    #parte 3  "analisis avanzado"


    #que pais genera mas ingresos?
# Ingreso por país
ingreso_pais = data.groupby("Pais").apply(lambda x: (x["Precio"] * x["Cantidad"]).sum()).reset_index(name="Ingreso")

# Ordenamos de mayor a menor ingreso
top_pais = ingreso_pais.sort_values(by="Ingreso", ascending=False)
print("País con más ingresos:\n", top_pais.head(1))
      
    #cual es la categoria con mayor ingreso promedio por venta?
data["Ingreso"] = data["Precio"] * data["Cantidad"]

prom_ingreso_categoria = data.groupby("Categoria")["Ingreso"].mean().reset_index()
top_categoria = prom_ingreso_categoria.sort_values(by="Ingreso", ascending=False)
print("Categoría con mayor ingreso promedio por venta:\n", top_categoria.head(1))

    #hay relacion entre el precio y la cantidad vendida?
correlacion = data["Precio"].corr(data["Cantidad"])
print("Correlación entre precio y cantidad vendida:", correlacion)

    #que dia de la semana se vende mas?
data["Día_semana"] = data["Fecha"].dt.day_name()
ventas_por_dia = data.groupby("Día_semana")["Cantidad"].sum().reset_index()
top_dia = ventas_por_dia.sort_values(by="Cantidad", ascending=False)
print("Día con más ventas:\n", top_dia.head(1))