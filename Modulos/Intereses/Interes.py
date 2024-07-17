def interesCompuesto(ci,i,y):
    interes = i/100
    return ci * (1 + interes)**y


def interesSimple(capitalInicial,tasa,tiempo):
    return capitalInicial*tasa*tiempo

def pagoMensual(total, meses, interes):
    interes = interes / 100
    pmt = (total * (1 + interes)) / meses
    return pmt


