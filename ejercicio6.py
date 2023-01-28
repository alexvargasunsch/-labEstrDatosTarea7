def dividirCadena(cadena,divisor):
    subcadena= cadena.split(divisor)
    return subcadena
def reemplazador (subcadena,remplazador):
    for i in range(len(subcadena)):
        if subcadena[i]== remplazador:
            subcadena1= input('Ingrese la nueva subcadena')
            subcadena[i]= subcadena1
    return subcadena

cadena= input('Ingrese una cadena: ')
divisor=input('Ingrese el caracter divisor: ')
subcadena= dividirCadena(cadena,divisor)
print(subcadena)
reemplazador1 = input('Ingrese la subcadena a ser reemplazado: ')
subcadenaReemplzado=reemplazador(subcadena, reemplazador1)
print(subcadenaReemplzado)