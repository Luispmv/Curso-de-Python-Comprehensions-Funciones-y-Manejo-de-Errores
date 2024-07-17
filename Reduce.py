# 9. Reduce
from functools import reduce

# Calcular la suma de una lista de números.
numeros = [1,2,3,4,5]
suma = reduce(lambda contador, iterable: contador + iterable, numeros )
print(suma)

# Encontrar el máximo de una lista de números.
numeros = [10,90,900,870]
mayor = reduce(lambda x, y: x if x > y else y, numeros)
print(mayor)


# Calcular el producto de una lista de números.
numbers = [1,2,3,4,5,6,7,8,9]
producto = reduce(lambda x, y: x * y, numbers)
print(producto)

# Concatenar una lista de cadenas en una sola cadena.
cadenas = ["Hola", "amigos", "como", "estan"]
concatenacion = reduce(lambda x, y: x + " " + y, cadenas)
print(concatenacion)


# Calcular la media de una lista de números.
numerillos = [10,20,30,40,50,60,70,80,90,100]
suma = reduce(lambda x,y: x + y, numerillos)
media = suma / len(numerillos)
print(media)


# Concatenar una lista de listas en una sola lista.
lista_listas = [[1,2,3,4,5], [1,2,3,4,5], [1,2,3,4,5]]
concat = reduce(lambda x, y: x + y, lista_listas)
print(concat)

