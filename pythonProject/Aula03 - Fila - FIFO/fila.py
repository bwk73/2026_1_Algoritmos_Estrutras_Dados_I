from No import No

class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print("------------------------------")
        print("Fila:")
        if self.inicio is None:
            print("Fila vazia!!!")
        else:
            aux = self.inicio
            txt = ""
            while aux:
                txt += aux.dado + " - "
                aux = aux.prox
            print(txt)
        print("------------------------------")

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.imprimir()

    def remover(self):
        if self.inicio is not None:
            self.inicio = self.inicio.prox
            if self.inicio is None:
                self.fim = None
            print("Elemento removido!")
        self.imprimir()