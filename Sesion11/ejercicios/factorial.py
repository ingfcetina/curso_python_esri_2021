#-------------------------------------------------------------------------------
# Name:        factorial.py
# Purpose:     Determinar el factorial de un numero
#
# Author:      ecetina@esri.co
#
# Created:     9/12/2021
# Copyright:   (c) Esri Colombia 2021
#-------------------------------------------------------------------------------

def calcularFactorial(numero):
    '''Calcula el factorial de un numero
    
    Parameters

    ----------
    numero : int
        numero para el que calcula el factorial
    ----------
    Returns
    int
        Devuelve un entero con el resultado del factorial
    '''
    print("Usted ingreso el nuumero: {}".format(numero))

    factorial = 1

    for i in range (1,numero+1):
        print ("revisemos como opera el ciclo...")
        print("i = {}, factorial: {}".format(i, factorial))
        factorial = factorial*i
        print("factorial = factorial * i ---- {}".format(factorial))
    print("el factorial del numero: {} es {}".format(numero,factorial))
    return factorial

calcularFactorial(5)