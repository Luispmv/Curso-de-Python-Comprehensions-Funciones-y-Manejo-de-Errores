# 16. Archivos .csv
import csv

def read_csv(ruta):
    try:
        with open(ruta, "r") as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            columna_name = next(reader)
            data = []
            for row in reader:
                union = zip(columna_name, row)
                dictionary = {key:value for key, value in union}
                data.append(dictionary)
            return data
    except FileNotFoundError as error:
        return error

call = read_csv("Archivos csv/data.csv")
print(call[0])

#Ejercicios con csv

# Escribe un programa que lea un archivo CSV llamado "datos.csv" y muestre su contenido en la consola
def showcsv(path):
    with open(path, "r") as csvdoc:
        return csvdoc.read()

call = showcsv("Archivos csv/data.csv")
print(call)

 


# Crea un programa que lea un archivo CSV, filtre las filas donde el valor en una columna "Edad" sea mayor a 30, y guarde las filas filtradas en un nuevo archivo llamado filtrado.csv
import csv
def mayores30(ruta):
    array_diccionario = []
    mas30 = []
    with open(ruta,"r") as csvfile:
        lectura = csv.reader(csvfile, delimiter=",")
        key = next(lectura)
        for value in lectura:
            key_value = dict(zip(key, value))
            array_diccionario.append(key_value)
    for item in array_diccionario:
        numberAge = int(item["Edad"])
        if numberAge > 30:
            mas30.append(item)
    with open("Archivos csv/Mayores30.csv","w",newline="") as csvdoc:
        escritor = csv.DictWriter(csvdoc, fieldnames=mas30[0].keys())
        escritor.writeheader()
        escritor.writerows(mas30)

    return "Archivo con las Edades Mayores a 30 agregado"


call = mayores30("Archivos csv/NombresEdades.csv")
print(call)



# Escribe un programa que lea un archivo CSV llamado notas.csv, calcule el promedio de los valores en la columna Nota y muestre el resultado.
import csv
def promedioCsv(path):
    suma = 0
    promedioEstudiantes = []
    with open(path,"r") as csvdoc:
        lectura = csv.reader(csvdoc, delimiter=",")
        llave = next(lectura)
        for valor in lectura:
            estudiantes = dict(zip(llave,valor))
            promedioEstudiantes.append(estudiantes)
    
    for promedio in promedioEstudiantes:
        notaInt = int(promedio["Nota"])
        suma += notaInt
    return f"El promedio de notas es de: {round(suma/len(promedioEstudiantes),1)}"
        

call = promedioCsv("Archivos csv/Notas.csv")
print(call)


# Crea un programa que lea un archivo CSV llamado ventas.csv, agrupe las ventas por la columna "Producto" y muestre la cantidad de ventas totales de todos los productos
import csv
def cantidadVentas(ruta):
    Productos = []
    suma = 0
    with open(ruta,"r") as ventascsv:
        csvFile = csv.reader(ventascsv,delimiter=",")
        columnas = next(csvFile)
        print(f"Las columnas existentes son {columnas}\n")
        for valor in csvFile:
            items = dict(zip(columnas,valor))
            Productos.append(items)
    for vendidos in Productos:
        print(vendidos["Producto"])
        unidades_venidas = int(vendidos["Unidades Vendidas"])
        suma += unidades_venidas
    return f"La venta total de todos los productos es de {suma}"



call = cantidadVentas("Archivos csv/Ventas.csv")
print(call)





# Escribe un programa que lea un archivo CSV llamado empleados.csv, calcule el salario anual de cada empleado (suponiendo que la columna "Salario Mensual") esta en el archivo, y guarde los datos en un nuevo archivo llamado "empleados_anual.csv" con una nueva columna "Salario Anual".
import csv
def calcularSalarioAnual(ruta):
    empleados = []
    with open(ruta,"r") as csvdoc:
        csvFile = csv.reader(csvdoc,delimiter=",")
        columnas = next(csvFile)
        for valor in csvFile:
            union = dict(zip(columnas,valor))
            #Convirtiendo a int el valor de Salario Mensual
            salario_mensual = int(union["Salario Mensual"])
            union["Salario Mensual"] = salario_mensual

            #Creando una columa de Salario Anual
            salario_anual = salario_mensual * 12
            union["Salario Anual"] = salario_anual
            empleados.append(union)

    #Guardando la columna "Salario Anual" en un archivo diferente
    with open("Archivos csv/Empleados_Anual.csv","w",newline="") as cvfile:
        escritor = csv.writer(cvfile)
        escritor.writerow(["Salario Anual"])
        for empleado in empleados:
            escritor.writerow([empleado["Salario Anual"]])

    return empleados

call = calcularSalarioAnual("Archivos csv/Empleados.csv")
print(call)






#Segunda solucion al ejercicio anterior
import csv

def calcularSalarioAnual(ruta_entrada, ruta_salida):
    empleados = []

    with open(ruta_entrada, "r", newline="") as csvdoc:
        csvFile = csv.DictReader(csvdoc)
        for row in csvFile:
            # Convirtiendo a int el valor de Salario Mensual
            salario_mensual = int(row["Salario Mensual"])

            # Creando una columna de Salario Anual
            salario_anual = salario_mensual * 12
            row["Salario Anual"] = salario_anual

            empleados.append(row)

    # Guardando la columna "Salario Anual" en un archivo diferente
    with open(ruta_salida, "w", newline="") as cvfile:
        fieldnames = ["Salario Anual"]  # Encabezado del archivo de salida
        escritor = csv.DictWriter(cvfile, fieldnames=fieldnames)
        escritor.writeheader()
        for empleado in empleados:
            escritor.writerow({"Salario Anual": empleado["Salario Anual"]})

    return empleados

# Ejemplo de uso
ruta_entrada = "Archivos csv/Empleados.csv"
ruta_salida = "Archivos csv/Empleados_Anualmente.csv"
empleados = calcularSalarioAnual(ruta_entrada, ruta_salida)
print(empleados)



