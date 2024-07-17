# SETS O CONJUNTOS

#Ejemplos de conjuntos
paises = {"Colombia", "Mexico", "Bolivia", "Brasil", "Brasil"}
print(paises)
print(type(paises))

numeros = {1,2,2,500,32}
print(numeros)
print(type(numeros))

tipos = {1,"Hola", False, 12.2}
print(tipos)
print(type(tipos))



#Ejemplo de la clase set
cadena_texto = "Hola"
cadena_texto_set = set(cadena_texto)
print("Conjunto => ",cadena_texto_set)
print(type(cadena_texto_set))



# De tupla a conjunto
tupla_ejemplo = ("Hola", "adios", "bye", "hi")
print("Ejemplo de tupla ==>", tupla_ejemplo)
set_tupla = set(tupla_ejemplo)
print("Conjunto ==> ",set_tupla)



# De lista a conjunto
numerillos = [1,2,2,3,3,3,4,5,5,6,6,6,6,7,8,9]
print("Lista con elementos reptidos => ", numerillos)

set_numerillos = set(numerillos)
print("Conjunto => ", set_numerillos)

numeros_unicos = list(set_numerillos)
print("Lista con elementos sin repetir => ",numeros_unicos)


# MODIFICANDO CONJUNTOS

#Imprimiendo el tamaño de un conjunto con len
jugadores_fut = {"messi", "cristiano", "neymar"}
print(len(jugadores_fut))

print("messi" in jugadores_fut)
print("rooney" in jugadores_fut)


#funcion add()
jugadores_fut.add("zlatan")
print(jugadores_fut)

#Funcion update()
ciudades = {"New York", "Mexico City", "Guadalajara"}
ciudades.update({"Munich", "Merida", "Chicago"})
print(ciudades)

#Funcion remove()
ciudades.remove("Munich")
print(ciudades)


#Funcion discard()
nombres = {"Manuel", "Mariano", "Eduardo", "Iñigo"}
nombres.discard("Pablo")
print(nombres)

#Funcion clear()
nombres.clear()
print(nombres)



# OPERACIONES CON CONJUNTOS

#UNION
conjunto_a = {"Messi", "Cristiano", "Neymar"}
conjunto_b = {"Messi", "Maradona", "Pele"}

conjunto_c = conjunto_a.union(conjunto_b)
print(conjunto_c)

nuevo_conjunto = conjunto_a | conjunto_b
print(nuevo_conjunto)



#INTERSECTION
conjunto_paises = {"Mexico", "Estados Unidos", "Canada", "Argentina", "Brazil"}
conjunto_paises_2 = {"Mexico","Argentina","Brazil"}

paises_latinos = conjunto_paises.intersection(conjunto_paises_2)
print(paises_latinos)
print("Usando and para la interseccion ==> ", conjunto_paises & conjunto_paises_2)


#DIFFERENCE
deportes = {"Futbol", "Basquetbol", "Tennis"}
deportes2 = {"Futbol"}
print(deportes - deportes2)

#SYMMETRIC DIFERENCE
marcas = {"Mcdonalds","Burger King", "Pizza hut"}
marcas_2 = {"Burger King", "Little Caesars", "Pizza hut"}

marca = marcas.symmetric_difference(marcas_2)
print(marca)




#PLAYGROUND
countries = {"MX", "COL", "ARG", "USA"}
northAm = {"USA", "CANADA"}
centralAm = {"MX", "GT", "BZ"}
southAM = {"COL", "BZ", "ARG"}

countries_uno = northAm.union(southAM)
new_Set = countries_uno.union(centralAm)
print(new_Set)






















#PRACTICAS

# Ejercicio 1: Crear y manipular conjuntos
# 	1.Crea dos conjuntos, conjunto_a y conjunto_b, con algunos elementos.
paises_set = {"Alemania", "Mexico", "China", "India", "España"}
ciudades_set = {"Munich", "Ciudad de Mexico", "Shangai", "Mumbai", "Madrid"}


# 	2.Agregar elementos a un conjunto:
ciudades_set.add("Nueva Dheli")
print(ciudades_set)

# 	3.Agrega el número 6 al conjunto_a.
paises_set.add(6)
print(paises_set)

# 	4.Eliminar elementos de un conjunto:
ciudades_set.remove("Nueva Dheli")
print(ciudades_set)







# Ejericio 2: Eliminar duplicados de una lista usando un conjunto

def eliminarDuplicados(lista):
    new_Set = set(lista)
    return list(new_Set)

duplicates = [1,2,3,4,5,6,7,8,8,8,8,9]

call = eliminarDuplicados(duplicates)
print(call)


# Ejercicio 3: Dada dos listas de números, encuentra los elementos comunes usando conjuntos


def elementosComunes(lista1, lista2):
    set1 = set(lista1)
    set2 = set(lista2)
    finalSet = set1.intersection(set2)
    return "Los elementos comunes son => ", finalSet


listado1 = [1,1,2,3,3,4,5,5,65,6,6,8]
listado2 = [1,2,2,2,3,3,3,4,5,5,7,8,9]
call = elementosComunes(listado1, listado2)
print(call)



#EJERCICIOS DE UNION

# 1. Crea dos conjuntos A y B con algunos números y encuentra la unión de ambos conjuntos

nsA = {1,2,3,4,5,6}
nsB = {1,9,8,7,6,4,2}
nsC = nsA.union(nsB)
print(nsC)

# 2. Crea tres conjuntos A, B y C con algunos números y encuentra la unión de los tres conjuntos

cA = {1,3,5,7,9}
cB = {2,4,6,8,10}
cC = {11,12,13,5,7,8}

unity = cA.union(cB)
finalU = unity.union(cC)
print(finalU)

# 3. Dada una lista de palabras únicas en ingles y otra lista de palabras únicas en español encuentra la unión de ambas listas para obtener un conjunto de palabras que incluya ambos idiomas.

english_set = {"Animal", "Capital", "Banana", "Doctor"}
conjunto_español = {"Mesa", "Silla", "Hola", "Doctor"}
conjunto_final = english_set.intersection(conjunto_español)
print("Esta palabra es la misma en ingles que en español => ", conjunto_final)

# 4. Dada una lista de estudiantes que asisten a una clase de matemáticas y otra lista de estudiantes que asisten a una clase de ciencias, encuentra la unión de ambas listas para obtener un conjunto de todos los estudiantes que asisten a alguna de las dos clases.

mate_students = {"Pablo", "Miguel", "Leo"}
science_students = {"Pablo", "Mariano", "Arath"}
all_students = mate_students.union(science_students)
print(all_students)

# 5. Crea dos conjuntos A y B, realiza la unión de ambos, y luego elimina un elemento específico del conjunto resultante.

cjA = {1,2,3,4,5,6,7,8,9}
cjB = {100,4,5,6,7,8,9,9,45}
cjC = cjA.union(cjB)

numero_usuario = int(input("Ingresa un numero: "))

if numero_usuario in cjC:
    print(cjC)
    cjC.remove(numero_usuario)
    print(numero_usuario, " ha sido eliminado")
    print(cjC)
else:
    print("No se encuentra aqui")


# 6. Crea dos conjuntos A y B, realiza la unión de ambos, y luego agrega un nuevo elemento al conjunto resultante.

scA = {1,2,3,4}
scB = {1,54,67}
scC = scA.union(scB)
scC.add("Hola")
print(scC)



# 7. Crea dos conjuntos A y B, realiza la unión de ambos, y luego verifica si un elemento específico pertenece al conjunto resultante.
conjuntazoA = {1,False, "Hola"}
conjuntazoB = {2, True, False}
conjuntazoC = conjuntazoA.union(conjuntazoB)

if False in conjuntazoC:
    print(True)
else:
    print(False)


# 8. Crea dos conjuntos A y B, realiza la unión de ambos, y determina el número total de elementos en el conjunto resultante.

cjtNA = {1,20,300,4000,5000}
cjtnB = {1000,900,80,7}
cjtnC = cjtNA.union(cjtnB)
print(cjtnC)
print(len(cjtnC))

# 9. Crea un conjunto A con algunos números y un conjunto B que esté vacío. Realiza la unión de ambos conjuntos y observa el resultado.

elementosA = {200,200,300,600,800}
elementosB = set()
elementosC = elementosA.union(elementosB)
print(elementosC)

# 10. Crea dos conjuntos A y B que estén vacíos, realiza la unión de ambos y observa el resultado.
cA1 = set()
cB2 = set()
cC3 = cA1.union(cB2)
print(cC3)







#INTERSECCION

A = {"cat", "dog", "mouse"} 
B = {"dog", "mouse", "elephant"}
C = A.intersection(B)
print(C)


#DIFFERENCE
perros = {"Pug", "Labrador", "Huski", "Dalmata"}
perros_2 = {"Pug", "Labrador"}
perrillos = perros.difference(perros_2)

print(perrillos)


#SYMMETRIC DIFFERENCE
animales = {"Leon", "T-Rex", "Pato"}
animales_2 = {"Leon", "Pato", "Burro"}
animales_3 = animales.symmetric_difference(animales_2)
print(animales_3)