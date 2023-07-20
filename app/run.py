import app.tree as trees
import random as randi
def run():
    print('Bienvenido al programa')
    arbolito = trees.AVLArbol()
    arbolito.insertar(15)
    arbolito.insertar(20)
    arbolito.insertar(40)
    arbolito.insertar(30) 
    arbolito.insertar(50)
    arbolito.insertar(25)
    arbolito.mostrar()
    #Buscar elemento
    buscame = 20
    resultado = arbolito.busqueda(20)
    if resultado:
        print("Encontrado")
    else:
        print('No encontrado')

    #eliminar elemento
    arbolito.eliminar(30)
    print('eliminado el 30')
    arbolito.mostrar()
    print('finalizacion del programa')

if __name__=='__main__':
    run()