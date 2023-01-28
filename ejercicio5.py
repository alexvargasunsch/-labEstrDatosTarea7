def dividirCadena(cadena,divisor):
    resultado= cadena.split(divisor)
    return resultado
def longitudSubcadena(subcadena):
    for i in range (len(subcadena)):
        longitud = subcadena[i]
        if longitud.isdecimal() is True:
            print ('La loguitud de la subcadena {} es {}'.format(longitud, len(subcadena)))

cadena= input('Ingrese la cadena: ')
divisor=input('Ingrese el caracter divisor: ')
subcadena= dividirCadena(cadena,divisor)
print(subcadena)