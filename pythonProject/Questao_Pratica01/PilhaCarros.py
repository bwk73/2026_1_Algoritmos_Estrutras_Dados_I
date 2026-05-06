from Carro import Carro

class PilhaCarros:
    def __init__(self):
        self.topo = None

def printCarro(self):
    print("---------------------------------")
    if self.topo is None:
        print("\nPilha de carros vazia!")
    else:
        print("\nPilha de Carros:")
        aux = self.topo
        while aux:
            print(aux)
            aux = aux.prox
    print("---------------------------------")

def addCarro(self, carro):
    if self.topo is not None:
        carro.prox = self.topo
    self.topo = carro
    self.printCarro()

def remCarro(self):
    if self.topo is not None:
        aux = self.topo
        self.topo = self.topo.prox
        del (aux)
    self.imprimir()