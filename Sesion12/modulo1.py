print ("cual es el valor de la palabra reservada __name__: {}".format(__name__))

def ejemplo1():
    return ("otro string")

def main():
    print("Esta es la funcion main")
    llamadofuncion = ejemplo1()
    return llamadofuncion

if __name__ == '__main__':
    print("Ejecuta logica de codigo, y la funcion main")
    resultado = main()
    print (resultado)