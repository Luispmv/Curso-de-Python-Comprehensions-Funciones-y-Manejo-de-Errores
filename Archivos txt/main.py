# 15. Archivos .txt

#Ejemplo 1 Abriendo y Leyendo un archivo con read() y leyendo cada linea de este con readline()

file = open("Archivos txt/didYouKnow.txt")
print(file.read())

print(file.readline())
print(file.readline())
print(file.readline())

file.close()

#Ejemplo 2 Abriendo un archivo e imprimiendo cada linea

with open("Archivos txt/didYouKnow.txt") as doc:
    for line in doc:
        print(line)


#Ejemplo 3 Abriendo un archivo, imprimiendo cada linea y escribiendo una linea
with open("Archivos txt/EscribirTexto.txt", "r+") as archivo:
    for line in archivo:
        print(line)
    archivo.write("\nAgregando nueva linea")


#Ejemplo 4 Sobreescribiendo un archivo al abrirlo y escribiendo sobre este
with open("Archivos txt/wWork.txt", "w+") as wdoc:
    for line in wdoc:
        print(line)
    wdoc.write("\n")
    wdoc.write("Modificando el archivo con w+")
    
    # Cambiamos la posicion del puntero de lectura o escritura con seek
    wdoc.seek(0)
    print(wdoc.read())



#Ejercicios con read()

# Crea una función que tome como parámetro una ruta y con esto abra un archivo de texto en donde lea todo su contenido. Imprime el contenido

def readFile(path):
    lista = []
    with open(path) as file:
        file.seek(0)
        for line in file:
            lista.append(line)
    return lista 

ruta = "Archivos txt/wWork.txt"
call = readFile(ruta)
print(" ".join(call))

  
# Abre un archivo de texto y lee todo su contenido. Cuenta y muestra el numero de palabras en el archivo
def countLineFile(path):
    counter = 0
    words = []
    with open(path) as file:
        content = file.read()
        for w in content.split():
            words.append(w)
            counter+= 1
    join_words = "\n".join(words)
    return f"Las palabras son:\n{join_words}\nson {counter} palabras en total en el archivo:\n\n{content}"

ruta = "Archivos txt/wWork.txt"
call = countLineFile(ruta)
print(call)



# Abre un archivo de texto y lee todo su contenido. Cuenta y muestra el numero de líneas en el archivo (usa el método Split('\n'))
def fileLines(path):
    counter = 0
    with open(path,"r") as docfile:
        contenido = docfile.read()
        lineas = contenido.split("\n")
        for item in lineas:
            print(item)
            counter += 1
    return counter
 
ruta = "Archivos txt/wWork.txt"
call = fileLines(ruta)
print(call)


# Abre un archivo de texto y lee todo su contenido. Busca una palabra especifica y muestra cuantas veces aparece en el archivo.
def wordFile(path, word):
    counter = 0
    with open(path,"r") as file:
        contenido = file.read()
        print(contenido)
        paragraphs = contenido.split()
        for item in paragraphs:
            if item == word:
                counter += 1
        
        if counter > 0:
            return f"'{word}' se encuentra {counter} veces en el texto"
        else:
            return f"{word} no se encuentra en el texto"

ruta = "Archivos txt/wWork.txt"
palabra = "archivo"
call = wordFile(ruta, palabra)
print(call)


# Abre un archivo de texto y lee todo su contenido. Convierte el 1contenido a mayúsculas y muestra el resultado.
def mayusFile(path):
    with open(path,"r") as document:
        contenido = document.read()
        mayusDocument = contenido.upper()
        return(mayusDocument)

ruta = "Archivos txt/wWork.txt"
call = mayusFile(ruta)
print(call)




#Ejercicios con readline()
# Abre un archivo de texto y usa readline() par leer la primera linea. Muestra la linea leida 

def firstLine(path):
    with open(path,"r") as archivo:
        return archivo.readline()

ruta = "Archivos txt/wWork.txt"
call = firstLine(ruta)
print(call)



# Abre un archivo de texto y usa readline() para leer las primeras N líneas. Muestra cada linea leida


def readLines(path, n):
    numeros_lineas = 0
    with open(path,"r") as archivo:
        for line in archivo:
            print(line.strip())
            numeros_lineas += 1
            if numeros_lineas >= n:
                break
    return f"\nSe han impreso {numeros_lineas} lineas"

ruta = "Archivos txt/wWork.txt"
call = readLines(ruta,3)
print(call)



# Abre un archivo de texto y usa readline() para leer linea por linea. busca una palabra especifica en cada linea y muestra en que líneas aparece
def wordSearching(path, lineN, word):
    counter = 0
    lineaFound = 0
    lineasFound = []
    try:
        with open(path,"r") as file:
            for _ in range(lineN):
                linea = file.readline()
                print(linea)
                for item in linea.split():
                    if item == word:
                        counter += 1
                        lineaFound = _+1
                        lineasFound.append(lineaFound)
            print("\n")
            if counter > 0:
                return f"'{word}' fue encontrada en {counter} ocasiones en las lineas: {lineasFound}"
            else:
                return f"{word} no fue encontrada en ninguna linea del archivo"
    except FileNotFoundError as error:
        return error

ruta = "Archivos txt/wWork.txt"
call = wordSearching(ruta,5,"Messi")
print(call)


# Abre un archivo de texto y usa readline() para leer la primera linea. Cuenta y muestra al numero de caracteres en esa linea.
def firstLineReading(path):
    with open(path,"r") as file:
        primera_linea = file.readline()
        items = [item for item in primera_linea.split()]
        itemsCount = sum([item.count(item) for item in primera_linea.split()])
        return f"Existen {itemsCount} caracteres y son: {items}"

ruta = "Archivos txt/wWork.txt"
call = firstLineReading(ruta)
print(call)


