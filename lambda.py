# 5. Funciones lambda 

# Suma de dos números:
# Crea una función lambda que tome dos números y devuelva su suma.

suma = lambda x , y : x + y
call = suma(20,20)
print(call)

# Producto de dos números:
# Crea una función lambda que tome dos números y devuelva su producto.
producto = lambda x, y : x * y
call = producto(20, 30)
print(call)


# Verificar si un número es par:
# Crea una función lambda que tome un número y devuelva True si es par y False si es impar.
espAR = lambda x: x % 2 == 0
call = espAR(3)
print(call)

# Obtener la longitud de una cadena:
# Crea una función lambda que tome una cadena y devuelva su longitud.
lenCadena = lambda cadena: f"La longitud de la cadena es {len(cadena)}"
call = lenCadena("Amigable")
print(call)


# Convertir una cadena a mayúsculas:
# Crea una función lambda que tome una cadena y la devuelva en mayúsculas.
mayusConverter = lambda chain: chain.upper()
call = mayusConverter("amor")
print(call)


# Filtrar números pares de una lista:
# Usa una función lambda con filter para obtener solo los números pares de una lista.
numeros = [1,2,3,4,5,6,7,8,9,10]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)


# Elevar al cuadrado los números de una lista:
# Usa una función lambda con map para obtener el cuadrado de cada número en una lista.
numeros = [2,5,7,45,90]
cuadrados = list(map(lambda x: x**2, numeros))
print(cuadrados)

# Verificar si un número es positivo, negativo o cero:
# Crea una función lambda que tome un número y devuelva "positivo" si el número es mayor que cero, "negativo" si es menor que cero, o "cero" si es igual a cero.
numeropnz = lambda x: "positivo" if x > 0 else ('negativo' if x < 0 else 'cero')

call = numeropnz(0)
print(call)


# Determinar la longitud de una cadena y categorizarla:
# Crea una función lambda que tome una cadena y devuelva "corta" si la longitud es menor que 5, "media" si la longitud está entre 5 y 10, o "larga" si la longitud es mayor que 10.
longitudCadena = lambda x : "corta" if len(x) < 5 else ("media" if len(x) > 5 and len(x) < 10 else "larga")

call = longitudCadena("Amabilidad")
print(call)

# Comparar dos números:
# Crea una función lambda que tome dos números y devuelva "mayor" si el primer número es mayor que el segundo, "igual" si son iguales, o "menor" si el primer número es menor que el segundo.
mayorNumero = lambda x,y: "mayor" if x > y else("igual" if x == y else "menor")
call = mayorNumero(9,9)
print(call)


# Categorizar una edad:
# Crea una función lambda que tome una edad y devuelva "niño" si la edad es menor que 12, "adolescente" si está entre 12 y 17, "adulto" si está entre 18 y 64, o "mayor" si es mayor o igual a 65.
edades = lambda edad: "niño" if edad < 12 else("adolescente" if edad >= 12 and edad <= 17 else("adulto" if edad >= 18 and edad <= 64 else "mayor"))

call = edades(4)
print(call)


# Determinar si un número es par o impar:
# Crea una función lambda que tome un número y devuelva "par" si el número es par y "impar" si es impar.
esParImpar = lambda x: "par" if x % 2 == 0 else "impar"
call = esParImpar(45)
print(call)


# Contar vocales en una cadena:
# Crea una función lambda que tome una cadena y cuente el número de vocales (a, e, i, o, u) que contiene.
vocalesCount = lambda x: sum(1 for char in x if char.lower() in 'aeiou')
call = vocalesCount("Hola amiguitos")
print(call)



# Calcular el área de diferentes formas geométricas:
# Crea funciones lambda separadas para calcular el área de un círculo, un triángulo y un rectángulo, pasando los parámetros necesarios.

#Area circulo
#pi por radio al cuadrado
areaCirculo = lambda x : round((3.1416 * x**2),2)
call = areaCirculo(20)
print(call)

#Area Triangulo
#base por altura entre dos 
areaTriangulo = lambda x, y: x * y / 2
call = areaTriangulo(20, 20)
print(call)

#Area rectangulo
#base por altura
areaRectangulo = lambda x,y: x * y
call = areaRectangulo(20.67)
print(call)

# Filtrar nombres por longitud:
# Usa una función lambda con filter para filtrar una lista de nombres y obtener solo aquellos que tienen una longitud mayor que 5 caracteres.
lista_nombres = ["Hola", "muriel", "miguel", "parlamento", "arma"]
fiveCharacters = list(filter(lambda x: len(x) > 5, lista_nombres))
print(fiveCharacters)
