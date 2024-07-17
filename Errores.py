# 13. Errores en Python

#Ejemplo 1
suma = lambda x,y: x + y
assert suma(2,2) == 6, "Resultado no esperado"

#Ejemplo 2
sumilla = lambda x, y: x + y
assert sumilla(2,2) == 4, "Resultado no esperado"
print(sumilla(2,2))


#Ejercicios con assert
#Verifica que la suma de dos numeros enteros sea igual a un valor esperado
sumilla = lambda a,b: a + b
assert sumilla(5,5) == 9, "Resultado inesperado"

#Asegurate de que una variable sea de un tipo de datos especifico (por ejemplo , "int" ,"float", "list")
entero = 90.1
assert isinstance(entero, int), "La variable no es un entero"

#Verifica que la longitud de una lista dada sea igua a un valor esperado
dieznumeros = [1,2,3,4,5,6,7,8,9,10]
assert len(dieznumeros) == 10, "No hay diez numeros"

#Asegurate de que una lista contenga un elemento especifico
listaNumeros = [2,4,6,8,10]
numero = 3
assert numero in listaNumeros, f"{numero} no se encuentra en {listaNumeros}"


#Verifica que un diccionario contenga una clave y valor especificos
jugadores = {
    "nombre": "Messi",
    "edad": 37
}
clave = "Calificacion"
assert clave in jugadores, f"{clave} no se encuentra en {jugadores}"
assert jugadores["edad"] == 37, "Esa no es la edad del jugador"

#Asegurate de que dos cadenas de texto sean iguales
cadena1 = "Amigo"
cadena2 = "Amigo"
assert cadena1 == cadena2, "Las cadenas no son iguales"

#Verifica que una lista contenga solo elementos unicos
lista = [1,2,3,4,5,6,6,7,8,9]
assert isinstance(lista, set), "La lista puede contener elementos repetidos"


#Verifica que una condicion booleana sea verdadera
edad = 17
assert edad >= 18 == True, "No es Mayor"

# Asegurate de que un numero este dentro de una rango especifico
numero = 98
rangoMenor = 1
rangoMayor = 50
assert numero in range(rangoMenor, rangoMayor), f"{numero} no esta entre {rangoMenor} y {rangoMayor}" 


#Ejemplo 3
age = 17
if age <= 17:
    raise Exception("No se permiten menores de edad")


# Crea una funcion que divida dos numeros y lanza una excepcion si el divisor es cero

def dividirNumeros(x, y):
    if y == 0:
        raise Exception("No se puede dividir entre cero")
    return round(x/y,2)

call = dividirNumeros(10,2.4)
print(call)


#Escribe una funcion que acceda a un elemento de una lista y lance una excepcion si un elemento esta fuera del rango
listiña = [1,2,3,41,5,6]
def elementoInList(lista, menor, mayor):
    inRange = []
    outOfRange = []
    for item in lista:
        if item in range(menor, mayor+1):
            inRange.append(item)
        else:
            outOfRange.append(item)
        
    if len(outOfRange) > 0:
        raise Exception("Hay al menos un elemento fuera de rango")
    else:
        return f"Todos los elementos se encuetran dentro de rango"

print(elementoInList(listiña, 1,41))

# Escribe una funcion que tome un numero como argumento y lance una excepcion si el numero es negativo
def esNegativo(number):
    if number < 0:
        raise Exception(f"{number} es un numero negativo")
    else:
        return f"{number} es un numero positivo"

print(esNegativo(9))


# Crea una funcion que solo acepte cadenas de texto como arguimento y lance una excepcion si se proporciona otro tipo de dato 

def onlyString(cadena):
    if isinstance(cadena, str):
        return f"El dato proporcionado es {type(cadena)}"
    else:
        raise Exception(f"El dato proporcionado es {type(cadena)}")

print(onlyString("Hola"))



#Escribe una funcion que verifique si una clave especifica esta presente en un diccionario y lance una excepcion si no lo esta
jugador = {
    "name":"messi",
    "edad": 37
}
def keyDict(key, dictionary):
    if isinstance(dictionary,dict):
        if dictionary[key]:
            return f"{key} se encuentra en {dictionary}"
        else:
            raise Exception(KeyError)
    else:
        return f"{dictionary} no es {dict}"
    
call = keyDict("name",jugador)
print(call)


# Escribe una funcion que tome una cadena y lance una excepcion si la longitud de la cadena es menor a un valor especifico
def cadenaLengthEspecifica(string, longitud):
    if len(string) < longitud:
        raise Exception(f"{string} es menor que la longitud dada: {longitud}")
    else:
        return f"{string} es mayor que la longitud dada: {longitud}"

print(cadenaLengthEspecifica("Hola", 8))

# Crea una funcion que tome un numero y lance una excepcion si el numero no esta dentro de un rango especificado
def numeroInRange(numero, menor, mayor):
    if numero in range(menor, mayor+1):
        return f"{numero} se encuentra dentro del rango {menor} a {mayor}"
    else:
        raise Exception(f"{numero} no se encuentra en el rango {menor} a {mayor}")

print(numeroInRange(21,1,20))


# Escribe una funcion que lance una excepcion si se proporciona una cadena vacia como argumento
def cadenaLength(cadena):
    if len(cadena) == 0:
        raise Exception("La cadena proporcionada esta vacia")
    else:
        return f"Cadena correcta"
