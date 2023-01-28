def palindromo (cadena):
    izquierda = 0 
    derecha = len(cadena) -1
    while derecha>= izquierda:
        if not cadena[izquierda] == cadena[derecha]:
            return False
        izquierda +=1
        derecha -=1
    return True

cadena = input('Ingrese la cadena de texto: ')

resultado = palindromo(cadena)
print('La palabra {} es palindromo: {}'.format(cadena, resultado))


