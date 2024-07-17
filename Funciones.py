# 4. Funciones

# Escribe una función que reciba un arreglo y retorne la suma de todos sus elementos.
def sumarElementos(lista):
    suma = sum([x for x in lista])
    return suma

call = sumarElementos([1,2,3,4,5,6,7,8,9,10])
print(call)

# Escribe una función que reciba un arreglo de números y retorne el producto de todos sus elementos
def multiplicarElementos(lista):
    multiplicacion = [x*x for x in lista]
    return multiplicacion

call = multiplicarElementos([1,2,3,4,5])
print(call)

# Escribe una función que reciba un arreglo y retorne el valor máximo.
def maximoValor(lista):
    maximo = max([x for x in lista])
    return maximo

call = maximoValor([1,2,3,4,5,89,87,88,90])
print(call)


# Escribe una función que reciba un arreglo y retorne el valor mínimo
def valorMinimo(lista):
    minimo = min([x for x in lista])
    return minimo

call = valorMinimo([1,2,3,4,5,89,87,88,90])
print(call)


# Escribe una función que reciba un arreglo y retorne un nuevo arreglo con los elementos en orden inverso
def arregloInverso(lista):
    inverso = lista[::-1]
    return inverso

call = arregloInverso([1,2,3,4,5,6,7,8,9,20])
print(call)


# Escribe una función que reciba un arreglo y retorne un nuevo arreglo sin elementos duplicados
def noRepeat(lista):
    conjunto = set(lista)
    return list(conjunto)

call = noRepeat([1,2,3,4,5,6,6,6,6,7,8,9])
print(call)

# Escribe una función que reciba dos arreglos y retorne un nuevo arreglo intercalando sus elementos
def intercalacion(arr1, arr2):
    return [item for pair in zip(arr1, arr2) for item in pair]

call = intercalacion([1,3,5,7,9],[2,4,6,8,10])
print(call)


# Escribe una función que reciba un arreglo y retorne el segundo valor mas grande 
def segundoMaximo(lista):
    maximo = max(lista)
    valor = lista[0]
    for item in lista:
        if item > valor and item < maximo:
            valor = item
    return valor

call = segundoMaximo([1,2,3,4,5,89,87,88,90])
print(call)

# Escribe una función que reciba un string y determine si es un palíndromo (es decir, si se lee igual de izquierda a derecha que de derecha a izquierda).
def esPalindromo(string):
    lower = string.lower()
    reverse = lower[::-1]
    if lower == reverse:
        return "Es palindromo"
    else:
        return "No es palindromo"

call = esPalindromo("Anal")
print(call)


# Escribe una función que reciba un arreglo y un elemento y retorne el numero de veces que ese elemento aparece en el arreglo
import collections

def contarAparicion(lista):
    contador = collections.Counter(lista)
    return contador

call = contarAparicion([1,1,1,1,2,3,4,5,6,6,7,8,9])
print(call)







