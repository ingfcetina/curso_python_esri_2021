#-------------------------------------------------------------------------------
# Name:        palindromo.py
# Purpose:     Determinar si una palabra es palindromo
#
# Author:      ecetina@esri.co
#
# Created:     9/12/2021
# Copyright:   (c) Esri Colombia 2021
#-------------------------------------------------------------------------------

def determinarPalindromo(palabra):
    '''Determina si una palabra es palindromo o no
    
    Parameters

    ----------
    palabra : str
        palabra en español
    ----------
    Returns
    Boolean
        Devuelve True si la palabra es palindromo, False
        en caso contrario
    '''
    print("Usted ingreso la palabra: {}".format(palabra))
    cadenaReverse = palabra[::-1]
    print("palabra en modo reverse: {}".format(cadenaReverse))
    longitudCadena = len(palabra)
    listaPalindromo =[]
    for letra in range (0,longitudCadena):
        if palabra[letra] == cadenaReverse[letra]:
            print("agregando la letra: {} de la cadena, a la lista de verificacion de palindromo".format(palabra[letra]))
            listaPalindromo.append(palabra[letra])
    print ("Se finalizo la comprobacion del palindromo...")
    longitudListaPalindromo = len(listaPalindromo)
    print ("Lista Palindromo: {}".format(listaPalindromo))
    print ("Lista palabra incial: {}".format(palabra))
    if longitudCadena == longitudListaPalindromo:
        print("La palabra es un palindromo")
        return True
    else:
        print("La palabra no es un palindromo")
        return False


