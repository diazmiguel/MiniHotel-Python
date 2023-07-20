class Nodo:
    def __init__(self,clave):
        self.clave = clave #Clave para ordenar
        self.izq = None #Subarbol izq
        self.der = None #Subarbol derecho
        self.altura = 1 #Es el nivel mas bajo del arbol
    
    
#NO REQUIERE QUE EL NOMBRE DE LA CLASE SEA IGUAL AL ARCHIVO
class AVLArbol: #El nombre de la clase es el del archivo
    def __init__(self): #Cuando inicia 
        self.raiz = None 
    
    def insertar(self, clave):
        if not self.raiz:  #Si no tiene raiz va a tenerlo
            self.raiz = Nodo(clave)
        else: #Si tiene raiz va a subinsertar un self
            self.raiz = self.subinsertar(self.raiz, clave)

    def subinsertar(self, nodo, clave):
        if not nodo:
            return Nodo(clave)
        elif clave < nodo.clave:
            #insertamos clave en el subarbol izquierdo
            nodo.izq = self.subinsertar(nodo.izq, clave)#De forma recursiva en la izq
        else:
            #Insertamos clave en el subarbol derecho
            nodo.der = self.subinsertar(nodo.der, clave)

        #Actualizamos la altura tras insertar la clave
        nodo.altura = 1 + max(self.getAltura(nodo.izq), self.getAltura(nodo.der))#Cual es el valor mas alto?    
        #Comprobamos el balance, y realizamos rotaciones si son necesarias
        balanceFactor = self.getBalance(nodo)

        if balanceFactor > 1:
            if clave < nodo.izq.clave:
                # rotacion simple izq-izq
                return self.rotacionDerecha(nodo)
            else:
                #rotacion doble izq-der
                nodo.izq= self.rotacionIzquierda(nodo.izq)
                return self.rotacionDerecha(nodo)   
        if balanceFactor < -1:
            if clave > nodo.der.clave:
                #rotacion simple der-der
                return self.rotacionIzquierda(nodo)
            else:
                #rotacion doble der-izq
                nodo.der = self.rotacionDerecha(nodo.der)
                return self.rotacionIzquierda(nodo)
        return nodo
    
    #NUEVAS ACTUALIZACIONES
    def busqueda(self, clave):
        return self.subbusqueda(self.raiz, clave)
    
    #Def subbusqueda, eliminar and subeliminar
    def subbusqueda(self, nodo, clave):
        if not nodo or nodo.clave == clave:
            return nodo
        if clave < nodo.clave:
            return self.subbusqueda(nodo.izq, clave)
        return self.subbusqueda(nodo.der, clave)

    def eliminar(self, clave):
        if not self.raiz:
            return
        self.raiz = self.subeliminar(self.raiz, clave)

    def subeliminar(self, nodo, clave):
        if not nodo:
            return nodo
        elif clave < nodo.clave:
            nodo.izq = self.subeliminar(nodo.izq, clave)
        elif clave > nodo.clave:
            nodo.der = self.subeliminar(nodo.der, clave)
        else:
            if not nodo.izq:
                return nodo.der
            elif not nodo.der:
                return nodo.izq
            else:
                sucesor = self.getMenor(nodo.der)
                nodo.clave = sucesor.clave
                nodo.der = self.subeliminar(nodo.der, clave)

        nodo.altura = 1 + max(self.getAltura(nodo.izq),self.getAltura(nodo.der))

        balanceFactor = self.getBalance(nodo)

        if balanceFactor > 1:
            if self.getBalance(nodo.izq) >= 0:
                return self.rotacionDerecha(nodo)
            else:
                nodo.izq = self.rotacionIzquierda(nodo.izq)
                return self.rotacionDerecha(nodo)
        if balanceFactor < -1:
            if self.getBalance(nodo.der) <= 0:
                return self.rotacionIzquierda(nodo)
            else:
                nodo.der = self.rotacionDerecha(nodo.der)
                return self.rotacionIzquierda(nodo)

    def getAltura(self, nodo):
        if not nodo:
            return 0
        return nodo.altura
    
    def getBalance(self, nodo):
        if not nodo:
            return 0 
        return self.getAltura(nodo.izq) - self.getAltura(nodo.der)

    def rotacionIzquierda(self, p):
        q = p.der
        h = q.izq 
        #Cambio
        q.izq = p
        p.der = h
        #actualizando alturas
        p.altura= 1 + max(self.getAltura(p.izq),self.getAltura(p.der))
        q.altura= 1 + max(self.getAltura(q.izq),self.getAltura(q.der))
        return q
    
    def rotacionDerecha(self, p):
        q = p.izq
        h = q.der 
        #Cambio
        q.der = p
        p.izq= h
        #actualizando alturas
        p.altura= 1 + max(self.getAltura(p.izq),self.getAltura(p.der))
        q.altura= 1 + max(self.getAltura(q.izq),self.getAltura(q.der))
        return q

    #modulo que permite obtener el menor de los mayores
    def getMenor(self,nodo):
        actual = nodo
        while actual.izq:
            actual = actual.izq
        return actual
    
    def mostrar(self):
        self.mostrarArbol(self.raiz)

    def mostrarArbol(self,nodo):
        if nodo:
            #InterOrden
            self.mostrarArbol(nodo.izq)
            print(nodo.clave)
            self.mostrarArbol(nodo.der)

