#Celsius a Fahrenheit
def cf(number):
    return (number * (9/5)) + 32

#Fahrenheit a Celsius
def fc(number):
    return round((number - 32) * (5/9),2)


#Kilometros a Millas
def km(number):
    return round(number * 0.621371,3)


#Millas a Kilometros
def mk(number):
    return round(number * 1.60934)
