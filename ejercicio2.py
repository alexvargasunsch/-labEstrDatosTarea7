def dividirCadena(cadena,divisor):
    subcadena= cadena.split(divisor)
    return subcadena
def subcadena(subcadena):
    for i in range(0,len(subcadena)):
        subcadena1= subcadena[i]
    return subcadena1

def longitud(subcadena):
    for i in range(len(subcadena)):
        contador = len(subcadena)
        if subcadena [i]== subcadena[i-1]:
            contador -= 1
    return contador
cadena= input('Ingrese una cadena: ')
divisor=input('Ingrese el caracter divisor: ')
subcadena1= dividirCadena(cadena,divisor)
subcadena2= subcadena(subcadena1)
longitud1= longitud(subcadena2)
print('las subcadenas no repetidas {} tiene {} numeros de carcteres'.format(subcadena2,longitud1))