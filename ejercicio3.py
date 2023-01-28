def dividirCadena(cadena,divisor):
    ressultado= cadena.split(divisor)
    return ressultado
cadena= input('Ingrse una cadena: ')
divisor=input('Ingrese el caracter divisor: ')
subcadena= dividirCadena(cadena,divisor)
print(subcadena)