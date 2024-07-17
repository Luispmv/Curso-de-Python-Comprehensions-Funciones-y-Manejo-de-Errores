# 14. Manejo de excepciones


# Division entre cero: Intenta dividir dos numeros: donde el segundo numero es cero

try:
    print(0/0)
except ZeroDivisionError as error:
    print(error)


# Indice fuera de rango: Intenta acceder a un elemento de una lista utilizando un indice que esta fuera del rango de la lista

nombres = ["Juan", "Miguel", "Ander"]
try:
    tercerElemento = print(nombres[3])
except IndexError as error:
    print(error)

# Conversion de tipo: Intenta convertir una cadena que no representa un numero en un entero utilizando int() y maneja la excepcion que ocurre
try:
    cadena = "Hola"
    numero = int(cadena)
except ValueError as error:
    print(error)



# Lectura de archivo inexistente: Intenta abrir un archivo que no existe en el sistema y maneja la excepcion
try:
    file = open("Hola.txt","r")
    print(file.read())
except FileNotFoundError as error:
    print(error)



# KeyError en diccionario: Intenta Acceder a una clave que no existe en un diccionario y maneja la excepcion keyError
try:    
    pais = {
        "Nombre":"Mexico",
        "Continente":"America",
        "Poblacion": 160000000
    }
    print(pais["Idioma"])
except KeyError as error:
    print(error)


# Entrada de usuario no numérica: Pide al usuario que ingrese un número, intenta convertirlo a int y maneja la excepción si el usuario ingresa algo que no es un número.
try:
    usuario = int(input("Ingresa un numero"))
except ValueError as error:
    print(error)


# División por cadena: Intenta dividir una cadena por otra cadena y maneja la excepción que se produce.
try:    
    cadena1 = "Hola"
    cadena2 = "Amigo"
    print(cadena1/cadena2)
except TypeError as error:
    print(error)

# Uso incorrecto de índice en una cadena: Intenta acceder a un carácter de una cadena utilizando un índice negativo y maneja la excepción que ocurre.
try:
    numeros = [1,2,3,4,5,6]
    print(numeros[-60])
except IndexError as error:
    print(error)

# Operación matemática inválida: Intenta realizar una operación matemática inválida, como sumar un número y una cadena, y maneja la excepción.
try:
    operacion = "Hola"/10
    print(operacion)
except TypeError as error:
    print(error)

# Uso incorrecto de función: Llama a una función con un número incorrecto de argumentos y maneja la excepción TypeError que se produce.

def suma(a,b):
    return a + b
try:
    suma(10,20,90)
    print(suma)
except TypeError as error:
    print(error)






