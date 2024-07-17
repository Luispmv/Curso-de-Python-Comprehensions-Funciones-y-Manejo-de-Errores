# 7. Map

# Aplicar una función que convierta una lista de cadenas a una lista de sus longitudes.
cadenas = ["Hola", "Mayor", "Amigo"]
longitudes_cadena = list(map(lambda x: len(x), cadenas))

print(longitudes_cadena)





# Convertir una lista de temperaturas en grados Celsius a grados Fahrenheit.
temperaturasCelsius = [10,20,40,50,90]
conversion = list(map(lambda x:x * (9/5) + 32,temperaturasCelsius))
print(f"La lista en Fahrenheit es: \n{conversion}")





# Dado una lista de nombres en minúsculas, convertir cada nombre a mayúsculas.
minusculas = ["Luis", "Fernando", "Joey", "Chandler"]
mayusculas = list(map(lambda name: name.upper(), minusculas))
print(mayusculas)





# Dado una lista de cadenas que representan números, convertir cada cadena a un número entero.
cadenas_numericas = ["1","13","30","50","100"]
cadenas_int = list(map(lambda x: int(x), cadenas_numericas))
print(cadenas_int)





# Aplicar una función que tome una lista de cadenas y devuelva una lista con la primera letra de cada cadena en mayúsculas.
lista_cadenas = ["Facebook", "Amazon", "Netflix", "Google"]
primeraLetra = list(map(lambda x: x[0], lista_cadenas))
print(primeraLetra)





# Dado una lista de listas de números, calcular la suma de cada sublista.
# Convertir una lista de números en una lista de sus valores absolutos.
lista_nums = [[1,2,3,4], [1,2,3,4,5], [10,20,90,78]]

suma_sublistas = list(map(lambda x: sum(x), lista_nums))
print(suma_sublistas)





# Dada una lista de palabras, devolver una lista de booleanos indicando si cada palabra tiene una longitud mayor que 5.
lista_palabras = ["ola", "amigable", "tilin"]
longitud5 = list(map(lambda x: True if len(x) > 5 else False, lista_palabras))
print(longitud5)




# Dadas dos listas de números del mismo tamaño, multiplica los elementos correspondientes de cada lista usando map con una función lambda.
lista1 = [1,3,5,7,9]
lista2 = [2,4,6,8,10]

multiplicacionListas = list(map(lambda x: x[0] * x[1], zip(lista1, lista2)))
print(multiplicacionListas)





# Utiliza map y range para calcular los cuadrados de los números del 1 al 10.
cuadrados = list(map(lambda x: x**2,range(1,11)))
print(cuadrados)




