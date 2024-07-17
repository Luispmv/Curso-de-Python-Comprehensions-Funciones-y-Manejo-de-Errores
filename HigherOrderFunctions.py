# 6. Higher Order Functions


# Escribe una función llamada "apply_function" que tome una función "f" y un valor "x" y devuelve el resultado de aplicar "f" a x

def sumar(x):
    return x + x*10

def apply_function(function, x):
    return x + function(x)

call = apply_function(sumar,20)
print(call)


# Escribe una función llamada apply_to_each que tome una función "f" y una lista "lst" y devuelva una nueva lista con "f" aplicado a cada elemento de "lst"

def pairs(lista):
    duplicada = [x*2 for x in lista]
    return duplicada

def apply_to_each(lista):
    funcionRecibida = pairs(lista)
    new_list = [x * 10 for x in funcionRecibida]
    return new_list

def callingLists(list):
    new_list = pairs(list)
    ten_duplicate_list = apply_to_each(new_list)
    return ten_duplicate_list

array = [1,2,3,4,5,6,7,8,9,10]
call = callingLists(array)
print(call)



# Escribe una función llamada filter_list que tome una función f y una lista lst, y devuelva una nueva lista con solo los elementos de lst para los cuales f devuelve True.

def Impar(x):
    impar = lambda x: True if x % 2 != 0 else False
    return impar(x)

call = Impar(5)
print(call)

def filter_list(lst):
    lista_impares = []
    for elemento in lst:
        if Impar(elemento):
            lista_impares.append(elemento)
        else:
            "No es impar"
    return lista_impares

call = filter_list([1,2,3,4,5,6,7,8,9,10,11])
print(call)