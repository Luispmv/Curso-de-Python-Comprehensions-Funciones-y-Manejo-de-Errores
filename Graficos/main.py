#17. Creación de graficos
import matplotlib.pyplot as plt

def graficaBarras(labels, values):
	fig, ax = plt.subplots()
	ax.bar(labels, values)
	plt.show()

def graficaPastel(labels, values):
	fig, ax = plt.subplots()
	ax.pie(values, labels=labels)
	ax.axis("equal")
	plt.show()

labels = ["a","b","c"]
values = [10,40,800]

graficaBarras(labels,values)
graficaPastel(labels,values)




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

# Grafico de Pastel
# Crea un grafico de pastel que muestre la distribución de ventas por categoría de productos

# Grafico de Dispersión
# Realiza un grafico de dispersión que muestre la relación entre el precio y la demanda de productos

# Grafico de Histograma:
# Representa la distribución de edades en una muestra de personas utilizando un histograma 