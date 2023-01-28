def frecuencia (cadena):
    diccionario ={}
    for i  in range (len(cadena)):
        elemento = cadena[i]
        frecuencia1 = cadena.count(elemento)
        diccionario.setdefault(elemento, frecuencia1)
    return diccionario
cadena = input('Ingrese una cadena: ')
diccionario = frecuencia(cadena)
print(diccionario)