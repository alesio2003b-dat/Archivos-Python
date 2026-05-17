###Ejercicios de la guía de Grafos
#Ejercicio 1
#Nodos
def crearnodos(*Nodos):
    nodos=[]
    for i in Nodos:
        nodos.append(i)
    return nodos

#Ejercicio 2
#Aristas
def creararista(*tuplas):
    aristas=[]
    for i in tuplas:
        aristas.append(i)
    return aristas

#Loa ejercicios 5 y 6 están más abajo 
class Nodo(object):
    def __init__(self, nombre):
        """Supone que el nombre es una cadena"""
        self._nombre = nombre

    def obtener_nombre(self):
        return self._nombre 
    def __str__(self):
        return self._nombre
    
    def __eq__(self, otro):
        return self._nombre==otro._nombre
    
    def __hash__(self):
        return hash(self._nombre)

class Arista(object):
    def __init__(self, origen, destino):
        """Supone que origen y destino son nodos"""
        self._origen = origen
        self._destino = destino

    def obtener_origen(self):
        return self._origen
    
    def obtener_destino(self):
        return self._destino
    
    def __str__(self):
        return self._origen.obtener_nombre() + '->' + self._destino.obtener_nombre()
    
    def __eq__(self, otro):
        return self._origen == otro._origen and self._destino == otro._destino 

class AristaPonderada(Arista):
    def __init__(self, origen, destino, peso=1.0):
        """Supone que origen y destino son nodos, peso es un número"""
        self._origen = origen
        self._destino = destino
        self._peso = peso

    def obtener_peso(self):
        return self._peso
    
    def __str__(self):
        return (f'{self._origen.obtener_nombre()}->({self._peso})' +
            f'{self._destino.obtener_nombre()}')

#Acá están los ejercicios 5 y 6
class GrafoDirigido(object):
    # nodos es una lista de los nodos en el grafo
    # aristas es un diccionario que asigna a cada nodo una lista de sus hijos
    def __init__(self,nodos=[],aristas=[]):
        self._nodos=[]
        self._aristas = {}
        for i in nodos:
            self.agregar_nodo(i)  
        for i in aristas:
            self.agregar_arista(i)
    
    def agregar_nodo(self, nodo):
        if nodo in self._nodos:
            raise ValueError('Nodo duplicado')
        else:
            self._nodos.append(nodo)
            self._aristas[nodo] = []
    
    def agregar_arista(self, arista):
        origen = arista.obtener_origen()
        destino = arista.obtener_destino()
        if not (origen in self._nodos and destino in self._nodos):
            raise ValueError('Nodo no está en el grafo')
        self._aristas[origen].append(destino)
    
    def hijos_de(self, nodo):
        return self._aristas[nodo]
    
    def tiene_nodo(self, nodo):
        return nodo in self._nodos
    
    def __str__(self):
        resultado = ''
        for origen in self._nodos:
            for destino in self._aristas[origen]:
                resultado = (resultado + origen.obtener_nombre() + '->'
                            + destino.obtener_nombre() + '\n')
        return resultado[:-1]  # omitir el salto de línea final
    def cantidad_nodos(self):
        return len(self._nodos)  
    def cantidad_aristas(self):
        return sum(len(arista) for arista in self._aristas.values())
    def grado(self,nodo):
        if nodo not in self._nodos:
            raise ValueError("Nodo no está en el grafo")
        else:
            return len(self._aristas[nodo])
    #Ejercicio 5
    def eliminar_arista(self, arista):
        origen = arista.obtener_origen()
        destino = arista.obtener_destino()
        if origen in self._aristas and destino in self._aristas[origen]:
            self._aristas[origen].remove(destino)
        else:
            raise ValueError('La arista no existe en el grafo')
    #Ejercicio 5
    def eliminarnodo(self,nodo):
        if nodo not in self._nodos:
            raise ValueError("El nodo no está en el grafo")
        self._nodos.remove(nodo)
        for i in self._nodos:
            self._aristas[i] =[x for x in self._aristas[i] if x!= i]
            self._aristas[nodo].pop()
    #Ejercicio 6
    def escamino(self, nodos):
        a=True
        for i in range(len(nodos)-1):
            if nodos[i+1] in  self._aristas[nodos[i]]:
                a=True
            else:
                a=False
                break
        return a
    def escaminosimple(self,nodos):
        b=nodos
        c=0
        for i in range(len(nodos)-1):
            if nodos[i+1] in  self._aristas[nodos[i]]:
                a=True
            else:
                a=False
                break
        if a==False:
            return a,c
        else:
            for i in nodos:
                b.remove(i)
                if i in b:
                    a=False
                    break
            return a
    def es_ciclo(self,nodos):
    # Verificar si la lista tiene al menos 3 nodos (para ser un ciclo)
        if len(nodos) < 3:
            return False
    # Verificar si el primer y último nodo son iguales (ciclo cerrado)
        if nodos[0] != nodos[-1]:
            return False
    # Verificar si todos los nodos son distintos
    #El set lo que hace es ponerlo como conjunto
        if len(set(nodos)) != len(nodos):
            return False
        return True
    def es_completo(self):
        for origen in self._nodos:
            for destino in self._nodos:
                if origen != destino:
                    if destino not in self._aristas[origen] and origen not in self._aristas[destino]:
                        return False
        return True
    #Ejercicio 15 (Lo saqué de la teoría)
    def dfs(self, actual, destino, camino_actual, visitados):
        visitados.append(actual)
        camino_actual.append(actual)

        if actual == destino:
            return camino_actual

        for vecino in self.hijos_de(actual):
            if vecino not in visitados:
                resultado = self.dfs(vecino, destino, camino_actual[:], visitados)
                if resultado:
                    return resultado
    #Ejercicio 16 (Lo saqué de la teoría)
    def encontrar_camino_bfs(grafo, inicio, fin):
        camino_inicial = [inicio]
        cola_caminos = [camino_inicial]
        while len(cola_caminos) != 0:
                # Obtener y eliminar el elemento más antiguo en la cola_caminos
                camino_tmp = cola_caminos.pop(0)
                ultimo_nodo = camino_tmp[-1]
                if ultimo_nodo == fin:
                        return camino_tmp
                for siguiente_nodo in grafo.hijos_de(ultimo_nodo):
                        if siguiente_nodo not in camino_tmp:
                                nuevo_camino = camino_tmp + [siguiente_nodo]
                                cola_caminos.append(nuevo_camino)
        return None
                
class GrafoDirigidoPonderado(GrafoDirigido):
    def agregar_arista(self, aristaPonderada):
        origen, destino, peso = aristaPonderada.obtener_origen(), aristaPonderada.obtener_destino(), aristaPonderada.obtener_peso()
        if origen not in self._nodos or destino not in self._nodos:
            raise ValueError('Uno de los nodos no está en el grafo')
        self._aristas[origen].append((destino, peso))
    def __str__(self):
        s = ''
        for nodo in self._nodos:
            for destino, peso in self._aristas[nodo]:
                s += f'{nodo} -> {destino} ({peso})\n'
        return s
    #Esto que está abajo creo que fue un intento de hacer DFS pero que me importen los pesos de las aristas, en plan el camino más corto que sea el que tenga la menor cantidad de peso
    # O sea que la suma de los pesos de las aristas sea la mínima, pero no me salió, asi que ignorenlo
    def DFS(self, inicio, fin, camino=[], peso=0,pesocorto=None, imprimir = False):
        """Supone que grafo es un GrafoDirigido; inicio y fin son nodos;
        camino y mas_corto son listas de nodos
        Devuelve un camino más corto desde inicio hasta fin en el grafo"""
        camino = camino + [inicio]
        lll=self._aristas[inicio]
        for i,j in lll:
            peso= peso + j
        if inicio == fin:
            return pesocorto
        for nodo in self.hijos_de(inicio):
            if nodo not in camino: # evitar ciclos
                if pesocorto is None or peso < pesocorto:
                    nuevo_camino = self.DFS(nodo, fin, camino, peso,pesocorto,imprimir)
                if nuevo_camino is not None:
                    pesocorto = nuevo_camino
        return camino,pesocorto

#Esto de acá abajo creo que es solo para probar como funcionaba todo
# n1=Nodo("a1")
# n2=Nodo("a2")
# n3=Nodo("a3")
# n4=Nodo("a4")
# n5=Nodo("a5")
# a1=Arista(n1,n2)
# a2=Arista(n2,n3)
# a3=Arista(n4,n1)
# a4=Arista(n3,n5)
# a5=Arista(n5,n1)
# g=GrafoDirigido([n1,n2,n3,n4,n5],[a1,a2,a3,a4,a5])
# # g.eliminararista(a1)
# nodos=[n1,n2,n3,n5,n1]
# print(g.escaminosimple(nodos))

# nodos=[0,1,2,3,4,5,6,7,8]
# arista=[1,2,3,4,5,6,7,8,9]
# a=GrafoDirigido(nodos,arista)
# print(a)

class Grafo(GrafoDirigido):
    def agregar_arista(self, arista):
        GrafoDirigido.agregar_arista(self, arista)
        rev = Arista(arista.obtener_destino(), arista.obtener_origen())
        GrafoDirigido.agregar_arista(self, rev)
    def eliminar_arista(self, arista):
        origen = arista.obtener_origen()
        destino = arista.obtener_destino()
        if origen in self._aristas and destino in self._aristas[origen]:
            self._aristas[origen].remove(destino)
        if destino in self._aristas and origen in self._aristas[destino]:
            self._aristas[destino].remove(origen)
        else:
            raise ValueError('La arista no existe en el grafo')


#Ejercicio 7
#El cuadrado con todas las lineas
A=Nodo("A")
B=Nodo("B")
C=Nodo("C")
D=Nodo("D")
E=Nodo("E")
a1=Arista(A,B)
a2=Arista(B,C)
a3=Arista(B,D)
a4=Arista(D,A)
a5=Arista(D,C)
a6=Arista(C,E)
a7=Arista(A,D)
#g=GrafoDirigido([A,B,C,D,E],[a1,a2,a3,a4,a5,a6,a7])
# print(g)
# print(g.cantidad_nodos())
# print(g.cantidad_aristas())
# print(g.grado(B))

#Ejercicio 8
# #Para que el grafo quede como en el Ejercicio 8 (solo las esquinas unidas)
# #Hay que eliminar las aristas a2,a6 y a7
# g.eliminar_arista(a2)
# g.eliminar_arista(a6)
# g.eliminar_arista(a7)
# print(g)

#Ejercicio 9
# # Para que quede como está en el Ejercicio 9 (con dos lineas cruzadas), hay que agregar dos nuevas aristas:
# a1=Arista(A,B)
# a3=Arista(B,D)
# a4=Arista(C,A)
# a5=Arista(D,C)
# a8=Arista(C,B)
# a9=Arista(A,D)
# g.agregar_arista(a8)
# g.agregar_arista(a9)
# print(g)

#Ejercicio 10
# #Comprobaciones (Ejercicio 10):
# g=GrafoDirigido([A,B,C,D,E],[a1,a3,a4,a5,a8,a9])
# print(g.escamino([C,B,A]))
# print(g.escamino([A,B,D,C,B]))
# print(g.escaminosimple([A,B,D,C,B]))
# print(g.escaminosimple([A,D,C,B]))
# print(g.es_ciclo([A,B,D,C,B]))
# print(g.es_ciclo([A,B,D,C,A]))
# print(g.es_completo())

#Ejercicio 11
#Grafo no dirigido (el del triangulo)
A=Nodo("A")
B=Nodo("B")
C=Nodo("C")
a1=Arista(A,B)
a2=Arista(B,C)
a3=Arista(C,A)
#d=Grafo([A,B,C],[a1,a2,a3])
#print(d)

#Ejercicio 12
#Para hacer el triangulo sin la conexion A-B, hay que eliminar la arista a1
#d.eliminar_arista(a1)
#print(d)
#MI CODIGO DE ELIMINAR ARISTA FUNCIONO VAMOOOOOOOOOOOOOOO

#Ejercicio 13
#Función Crear Grafo
def creargrafo(nombre):
    c=GrafoDirigidoPonderado()
    h=0
    with open(nombre,"r",encoding='utf-8') as algo:
        for i in algo:
            if h!=0:
                a=i.strip().split(";")
                nodo1=Nodo(str(a[0]))
                nodo2=Nodo(str(a[1]))
                d=float(a[-1])
                if nodo1 not in c._nodos:
                    c.agregar_nodo(nodo1)
                if nodo2 not in c._nodos:
                    c.agregar_nodo(nodo2)
                c.agregar_arista(AristaPonderada(nodo1,nodo2,d)) 
            h=h+1
        return c
hola=creargrafo("santa_fe.csv")
print(hola.DFS("Santa Fe Ciudad","Coronda"))

#print(creargrafo("santa_fe.csv"))

#Ejercicio 14 (Esta respuesta la saqué de una guía que subieron los profes con la resolución de los problemas de grafos)
#Función que calcula distancia
def calcular_distancia(grafo, camino):
    distancia = 0
    for i in range(len(camino) - 1):
        nodo_actual = camino[i]
        nodo_siguiente = camino[i + 1]
        arista = None
        for a in grafo._aristas[nodo_actual]:
            if nodo_siguiente == a[0]:
                arista = a
                break
        distancia += arista[1]
    return distancia
#Esa funcion debería de funcionar pero no sé como hacerla funcionar
#Los otros dos métodos ya están añadidos arriba.

#Si llegaron hasta acá es porque están en la ultima semana de cuatrimestre. Asi que muchos animos que ya es el último esfuerzo y se termina. Ustedes pueden :)
