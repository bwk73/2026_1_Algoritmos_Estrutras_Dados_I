from Apartamento import Apartamento
from Torre import Torre

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def add(self, ap):
        if self.inicio is None:
            self.inicio = ap
            self.fim = ap
        else:
            self.fim.proximo = ap
        self.fim = ap

    def imprimir(self):
        print("\n\n------------------------------")
        if self.inicio is None:
            print("Fila de apartamentos vazia!")
        else:
            aux = self.inicio
            while aux:
                print(aux)
                aux = aux.proximo
                print("\n\n------------------------------")

    def remover(self):
        if self.inicio is None:
            print("\nNão há apartamentos na fila!")
            return None
        else:
            print("Apartamento removido da fila: ")
            print(self.inicio)
            aux = self.inicio
            self.inicio = self.inicio.proximo
            if self.inicio is None:
                self.fim = None
            return aux