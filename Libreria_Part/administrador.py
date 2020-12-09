from .particula import Particula
import json 
from pprint import pprint
from pprint import pformat

class Administrador:
    def __init__(self):
        self.__particulas = []

    def agregar_final(self, particula:Particula):
        self.__particulas.append(particula)

    def agregar_inicio(self, particula:Particula):
        self.__particulas.insert(0, particula)

    def mostrar(self):
        for particula in self.__particulas:
            print(particula)

    def __str__(self):
        return "".join(
            str(particula) + '\n' for particula in self.__particulas
        )

    def __len__(self):
        return len(self.__particulas)

    def __iter__(self):
        self.cont = 0

        return self

    def __next__(self):
        if self.cont < len(self.__particulas):
            particula = self.__particulas[self.cont]
            self.cont += 1
            return particula
        else:
            raise StopIteration


    def guardar (self, ubicacion):
        try:
            with open(ubicacion, 'w') as archivo:
                lista = [particula.to_dict() for particula in self.__particulas]
                print (lista)
                json.dump(lista, archivo, indent=5)
            return 1
        except:
            return 0

    def abrir (self, ubicacion):
        try:
            with open (ubicacion, 'r') as archivo:
                lista = json.load(archivo)
                self.__particulas = [Particula(**particula) for particula in lista]
            return 1
        except:
            return 0

    def dictionary(self,grafo):

        for particula in self.__particulas:
            key = (particula.origen_x, particula.origen_y) 
            value = ((particula.destino_x, particula.destino_y), particula.distancia)
            key_2 = (particula.destino_x, particula.destino_y)
            value_2 = ((particula.origen_x, particula.origen_y), particula.distancia)
            if key in grafo:
                grafo[key].append(value)
            else:
                grafo[key] = [value]
            if key_2 in grafo:
                grafo[key_2].append(value_2)
            else:
                grafo[key_2] = [value_2]
        str = pformat(grafo, width=60, indent=2)
        return str

    def profundidad(self, grafo, origen_x=0, origen_y=0):
        self.dictionary(grafo)
        key = (origen_x, origen_y)

        if key in grafo:
            pila = []
            visitados = []
            recorrido = []

            pila.append(key)
            visitados.append(key)

            while len(pila) > 0:
                vertice = pila[-1]
                recorrido.append(vertice)
                pila.pop()
                adyacente = grafo[vertice]
                for i in adyacente:
                    if not i[0] in visitados:
                        visitados.append(i[0])
                        pila.append(i[0])
            return recorrido
        else:
            return 0