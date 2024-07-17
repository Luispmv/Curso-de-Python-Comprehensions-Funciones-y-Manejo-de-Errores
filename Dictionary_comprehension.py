# 3. Dictionary Comprehension

# Crea un diccionario con las letras del abecedario como claves y sus correspondientes valores como el índice de cada letra en el abecedario.
abecedario = 'abcdefghijklmnopqrstuvwxyz'
indice_letras = {letra: abecedario.index(letra) for letra in abecedario}
print(indice_letras)


# Dado un diccionario que contiene nombres de personas como claves y sus edades como valores, crea un nuevo diccionario que contenga solo las personas mayores de 18 años.
personas = {
    'Juan': 30,
    'María': 25,
    'Pedro': 35,
    'Ana': 28,
    'Carlos': 32
}

new_dict = {nombre: edad for nombre, edad in personas.items() if edad > 30}
print(new_dict)



# Convierte una lista de números en un diccionario donde las claves sean los números y los valores sean sus cuadrados.
numeros = [1,2,3,4,5,6,7,8,9,10]

cuadrados = {i: i**2 for i in numeros}
print(cuadrados)


# Dado un diccionario que contiene nombres de frutas como claves y sus precios como valores, crea un nuevo diccionario donde se multipliquen los precios por 1.1 para simular un aumento del 10%.

frutas = {
    "Platano":24,
    "Manzana":23,
    "Piña":23,
    "Sandia":23,
    "Melon":23,
}

frutas_new = {i:p*1.1 for i, p in frutas.items()}
print(frutas_new)

# Dada una lista de números, crea un diccionario donde las claves sean los números pares y los valores sean True si son números pares y False si no lo son.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
diccionario_pares = {i: True if i % 2 == 0 else False for i in numbers}
print(diccionario_pares)


# Convierte un diccionario que contiene nombres de estudiantes como claves y sus calificaciones como valores, a otro diccionario donde las claves sean las calificaciones y los valores sean listas de nombres de estudiantes que obtuvieron esa calificación.

estudiantes = {
    "Miguel":10,
    "Luis":6,
    "Dario":7,
    "Enzo":8
}

diccionario_calificaciones = {calificacion: [estudiante for estudiante, calif in estudiantes.items() if calif == calificacion] for calificacion in set(estudiantes.values())}

print(diccionario_calificaciones)


# Elevar al cuadrado los números de una lista y almacenarlos en un diccionario.
numerillos = [11,24,56,78,6,5,7,89,9]
numerillos_pow = {i:i**2 for i in numerillos}
print(numerillos_pow)



# Convertir una lista de strings en un diccionario donde las claves sean los strings y los valores sean sus longitudes.
strings = ["ola", "mariano", "juventus", "barcelona"]

string_dict = {item: len(item) for item in strings}
print(string_dict)


# Contar la frecuencia de cada letra en una cadena y almacenar los resultados en un diccionario.
cadenita = "Esta es una cadena de texto"
cadenita_Count = {i:cadenita.count(i) for i in set(cadenita)}
print(cadenita_Count)


# Invertir un diccionario dado, intercambiando las llaves y los valores.
futbolistas = {
    "messi":10,
    "CR7":7,
    "Neymar": 10,
    "Ibrahimovic": 9
}
new_futbolistas = {v:k for k,v in futbolistas.items()}
print(new_futbolistas)



# Filtrar un diccionario para obtener solo aquellos pares clave-valor donde el valor sea mayor o igual a un cierto umbral.
calificaciones =  {
    "alberto":10,
    "Mauricio":9,
    "Alan":5,
    "Daniel":4,
}

aprobado = {i:valor for i, valor in calificaciones.items() if valor > 5}
print(aprobado)

# Crear un diccionario donde las claves sean las primeras letras de las palabras en una lista y los valores sean las palabras completas.
words = ["Hola", "mujer", "marido", "orangutan"]

words_dict = {i[0]: i for i in words}
print(words_dict)

# Calcular las raíces cuadradas de los números en una lista y almacenar los resultados en un diccionario.
import math
numeros_raiz = [1,2,3,4,5,6,7,8,9,10]
raiz_dict = {i:math.sqrt(i) for i in numeros_raiz}
print(raiz_dict)

#Crear un diccionario con números del 1 al 10 y sus cubos.
numeros_lista = [1,4,17,19,3]
cubos = {i:i**3 for i in numeros_lista}
print(cubos)


# Crear un diccionario donde las claves sean nombres de personas y los valores sean sus edades. Luego encontrar la persona mas joven y la mas vieja.
nombres = ["Juan","Carlos", "Miguel", "Pablo", "Adme"]
calificaciones = [9,7,8,10,5]

estudiantes_grades = {i:c for i,c in zip(nombres, calificaciones)}
print(estudiantes_grades)

estudents_min = min(estudiantes_grades)
estudents_max = max(estudiantes_grades)
print(f"el peor es {estudents_min} y el mejor es {estudents_max}")



# Crear un diccionario donde las claves sean los nombres de los alumnos y los valores sean listas de sus calificaciones. Calcular la calificación promedio de cada alumno.
alumnos = ["Joey", "Chandler", "Monica", "Ross", "Rachel", "Phoebe"]
grades = [[6,6,7],[8,7,8],[10,10,10],[10,10,10],[9,9,8],[8,9,9]]

alumnos_grades = {a:g for a,g in zip(alumnos, grades)}
promedios = {a:round(sum(g)/len(g), 1) for a,g in alumnos_grades.items()}
print(promedios)



# Crear un diccionario para almacenar los contactos de un teléfono, donde las claves sean los nombres de las personas y los valores sean sus números de teléfono. Implementar una búsqueda para encontrar el número de una persona por su nombre.
contactos = ["Luis", "Uriel", "Diego", "Kevin", "Yahir"]
telefonos = [4776311039,477621097,4776802432,47725047890,47721406750]

telefonos_contacto = {c: t for c, t in zip(contactos, telefonos)}
print(telefonos_contacto)

usuario = input("Ingresa un nombre de contacto: ")
call = telefonos_contacto[usuario]
print(call)




# Dado un diccionario de productos y sus precios, crear un nuevo diccionario que contenga solo los productos cuyo precio esté por debajo de un cierto umbral.
productos = ["doritos", "sabritas", "fritos", "emperador", "principe"]
precios = [10,10,5,5,10]

inventario = {item:precio for item, precio in zip(productos, precios) if precio > 5}
print(inventario)


