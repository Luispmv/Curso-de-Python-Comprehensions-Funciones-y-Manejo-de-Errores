# 2. List Comprehension
# Genera una lista que contenga los cuadrados de los números del 1 al 10
numeros_cuadrado = [n**2 for n in range(1,11)]
print("List comprehension con numeros al cuadrado =>",numeros_cuadrado)


# Dada una lista de números, crea una nueva lista que contenga solo los números pares
numeros_pares = [n for n in range(1,11) if n%2==0]
print("List comprehension con numeros pares =>",numeros_pares)


# Dada una lista de temperaturas en grados Celsius, crea una nueva lista con las temperaturas convertidas a grados Fahrenheit

# 1 grado celsius = 33.8 grados Fahrenheit

lista_celsius = [1,80,56,87,89,45]

lista_fahrenheit = [(e * (9/5) + 32) for e in lista_celsius]
print("Lista fahrenheit => ", lista_fahrenheit)


# Dada una lista de palabras, genera una nueva lista con las longitudes de esas palabras
lista_palabras = ["manzana","banana","pera","piña","sandia"]
longitudes_lista = [len(n) for n in lista_palabras]
print("Longitudes lista => ", longitudes_lista)


# Dada una lista de palabras y una letra, crea una nueva lista con las palabras que comienzan con esa letra.
palabras_lista = ["Amor", "Arion", "Arma", "Love", "martillo"]
palabras_m = [p for p in palabras_lista if p.startswith("m")]
print("palabras que comenzan con m => ", palabras_m)


# Genera una lista de tuplas donde cada tupla contiene un numero y su cuadrado, para números del 1 al 10
tupla_cuadrados = [(n, n**2) for n in range(1,11)]
print("tupla cuadrados =>",tupla_cuadrados)

# Dada una cadena, crea una nueva cadena donde todas las vocales sean reemplazadas por asteriscos
cadena = "Hola"
asteriscos = ["x" * len(a) for a in cadena if a in "aeiou"]
print("remplazando vocales por asteriscos => ",asteriscos)

# Dada una lista de palabras, crea una nueva lista con el primer carácter de cada palabra
muchas_palabras = ["messi","cristiano","pele","maradona"]
primer_caracter = [n[0] for n in muchas_palabras]
print(primer_caracter)


# Genera una lista de números del 1 al 100 que sean divisibles por 3 y por 5
divisibles_tc = [n for n in range(1,101) if n%3 == 0 and n%5 == 0]
print(divisibles_tc)

# Dada una lista de palabras, crea una nueva lista con las palabras que tienen una longitud par.
palabras = ["amor", "hola", "romance", "ciencia"]
lista_par = [p for p in palabras if len(p)%2==0]
print("palabras longitud par => ",lista_par)


# Dada dos listas de números, genera una nueva lista que contenga la suma de los números correspondientes en las dos listas
l1 = [1,3,5,7,9]
l2 = [2,4,6,8,10]

sumas = [n + n2 for n, n2 in zip(l1,l2)]
print("Lista de resultados =>", sumas)


# Dada una lista de cadenas, crea una nueva lista con las mismas cadenas convertidas a mayúsculas
cadenas_lower = ["hola","como","estas","amigo"]
cadenas_upper = [n.upper() for n in cadenas_lower]
print(cadenas_upper)
