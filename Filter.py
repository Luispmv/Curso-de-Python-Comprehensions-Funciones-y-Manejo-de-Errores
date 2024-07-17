# 8. Filter

# Filtrar los números pares de una lista de enteros.
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)





# Filtrar los números impares de una lista de enteros.
numeros = [1,2,3,4,5,6,7,8,9,10]
inpares = list(filter(lambda x: x % 2 != 0, numeros))
print(inpares)





# Filtrar los strings que tienen más de 5 caracteres en una lista de strings.
lista_strings = ["Hola", "miguel", "marihuano", "araña"]
caracteres5 = list(filter(lambda x: len(x) > 5, lista_strings))
print(caracteres5)





# Filtrar los números negativos de una lista de números.
lista_numbers = [1,1,2,-6,9,7,-5]
negativos = list(filter(lambda x: x < 0, lista_numbers))
print(negativos)





# Filtrar los números mayores que 10 en una lista de números.
lista_numbers = [1,1,2,-6,9,7,-5,90,56]
mayores10 = list(filter(lambda x: x > 10, lista_numbers))
print(mayores10)





# Filtrar las palabras que empiezan con una vocal en una lista de palabras.
vocales = "aeiou"
lista_words = ["amigo", "Hola", "tilin", "oro"]
palabras_vocales = list(filter(lambda x: x[0] in vocales, lista_words))
print(palabras_vocales)





# Filtrar los números que son múltiplos de 5 en una lista de números.
numbers = [1,2,3,4,5,6,7,8,9,10]
multiplo5 = list(filter(lambda x: x % 5 == 0, numbers))
print(multiplo5)





# Filtrar las personas mayores de edad en una lista de tuplas (nombre, edad).
lista_t_edades = [("Luis", 21), ("Miguel", 17), ("Monica", 23), ("Mariano",18)]

mayores_de_edad = list(filter(lambda x: x[1] >= 18, lista_t_edades))
print(mayores_de_edad)





# Filtrar las palabras que contienen la letra 'a' en una lista de palabras.
palabras = ["miguel", "ariana", "phoebe"]
containsa = list(filter(lambda x: "a" in x , palabras))
print(containsa)

