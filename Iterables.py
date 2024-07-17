# 12. Iterables

# Número de elementos pares:
# Escribe una función que tome una lista de números y devuelva el número de elementos que son pares.

numeros = [1,2,3,4,5,6,7,8,9,10]

def countPairs(array):
    pares = list(filter(lambda x: x%2==0,numeros))
    return f"En {array} hay {len(pares)} pares y son {pares}"

call = countPairs(numeros)
print(call)

# Número de elementos impares:
# Escribe una función que tome una lista de números y devuelva el número de elementos que son impares.

def countOdds(array):
    impares = list(filter(lambda x: x%2!=0,numeros))
    return f"En {array} hay {len(impares)} impares y son {impares}"

call = countOdds(numeros)
print(call)


# Máximo y mínimo de los elementos:
# Escribe una función que tome una lista de números y devuelva el número máximo y el número mínimo de la lista.
def MaximoMinimo(array):
    biggest = array[0]
    lowest = array[0]
    for item in array:
        if item > biggest:
            biggest = item
    for item in array:
        if item < lowest:
            lowest = item
    
    return f"El mayor numero en {array} es {biggest} y el menor es {lowest}"

call = MaximoMinimo([1,2,3,4,5,6,78,87,54,65,65,89])
print(call)


# Contar ocurrencias de un elemento:
# Escribe una función que tome una lista y un valor, y devuelva el número de veces que ese valor aparece en la lista.

def ocurrenciasElemento(array, elemento):
    counter = 0
    for item in array:
        if item == elemento:
            counter += 1
    return f"{elemento} aparece {counter} veces en {array}"

arrey = [1,2,3,4,5,6,7,8,9,9]
print(ocurrenciasElemento(arrey, 9))




# Eliminar duplicados:
# Escribe una función que tome una lista y devuelva una nueva lista con todos los elementos únicos (sin duplicados).

def noDuplicados(lista):
    setLista = set(lista)
    return list(setLista)

call = noDuplicados([1,2,3,4,5,6,7,7,7,8,8,8,9])
print(call)


# Filtrar elementos mayores que un valor:
# Escribe una función que tome una lista de números y un valor, y devuelva una nueva lista con los elementos que son mayores que el valor dado.

def mayoresQue(lista, valor):
    mayores = []
    for item in lista:
        if item > valor:
            mayores.append(item)
    return mayores

numbers = [1,2,3,4,4,5,6,7,8,8,9,3]
call = mayoresQue(numbers, 7)
print(call)




# Ejercicios con Iter
iterable = iter(range(1,11))

print(next(iterable))
print(next(iterable))
print(next(iterable))
print(next(iterable))











