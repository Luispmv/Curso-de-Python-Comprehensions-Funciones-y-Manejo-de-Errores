def contarVocales(string):
    vocales = "aeiouAEIOU"
    counter = 0
    for item in string:
        if item in vocales:
            counter+= 1
    return f"La palabra {string} tiene {counter} vocales"

def palindromo(string):
    stringLower = string.lower()
    if stringLower == stringLower[::-1]:
        return True
    else:
        return False

def reversa(string):
    return string[::-1]  




