#17. Creación de graficos
import matplotlib.pyplot as plt

def graficaBarras(labels, values,titulo):
	fig, ax = plt.subplots()
	ax.bar(labels, values)
	ax.set_title(titulo)
	plt.show()

def graficaPastel(labels, values,titulo):
	fig, ax = plt.subplots()
	ax.pie(values, labels=labels)
	ax.set_title(titulo)
	ax.axis("equal")
	plt.show()

labels = ["a","b","c"]
values = [10,40,800]

graficaBarras(labels,values,"valores")
graficaPastel(labels,values, "valores")




#Ejercicios
# Grafico en linea
# Crea un grafico que muestre la evolución de ventas mensuales a lo largo del año
import matplotlib.pyplot as plt

def graficoLinea(etiquetas,valores):
    plt.plot(etiquetas, valores)
    plt.show()

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]
ventas = [1000,200,300,500,700,900,700,900,1200,1450,1320,9020]

graficoLinea(meses,ventas)

# Grafico de Barras
# Representa el rendimiento de diferentes equipos mediante un grafico de barras

equipos = ["Real Madrid","Barcelona","Atletico de Madrid","Liverpool","Manchester United"]
calificacion = [10,7,8,9,4]
graficaBarras(equipos,calificacion,"Rendimiento equipos")

# Grafico de Pastel
# Crea un grafico de pastel que muestre la distribución de ventas por categoría de productos
categoria = ["Electronico","Moda","Hogar","Panaderia","Carniceria","Comida"]
venta = [120000,60000,45000,32000,56000,200000]

graficaPastel(categoria, venta,"Distribucion de venta por categoria de productos")
