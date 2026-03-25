from No import No
# Lista Duplamente Encadeada por ordem de chegada

class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print("------------------------------")
        print("Lista Duplamente Encadeada por ordem de chegada:")
        if self.inicio is None:
            print("Lista vazia!!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.proximo
        print("------------------------------")

    def imprimirReverso(self):
        print("------------------------------")
        print("Lista Duplamente Encadeada por ordem REVERSA de chegada:")
        if self.inicio is None:
            print("Lista vazia!!!")
        else:
            aux = self.fim
            while aux:
                print(aux.dado)
                aux = aux.anterior
        print("------------------------------")

    def add(self, valor):
        nodo = No(valor)
        if self.inicio is None:     # se a lista estiver vazia
            self.inicio = nodo
        else:                       # se já houver 'alguém' na lista
            self.fim.proximo = nodo
            nodo.anterior = self.fim
        self.fim = nodo
        self.imprimir()