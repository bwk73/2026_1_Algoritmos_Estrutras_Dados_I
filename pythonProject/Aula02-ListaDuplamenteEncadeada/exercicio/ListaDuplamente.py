from No import No
# Lista Duplamente Encadeada por ordem alfabética:

class ListaDuplamente:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def imprimir(self):
        print("------------------------------")
        print("Lista Duplamente Encadeada por ordem alfabética:")
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
        print("Lista Duplamente Encadeada por ordem alfabética REVERSA:")
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
            self.fim = nodo
        else:                       # se já houver 'alguém' na lista
            if nodo.dado < self.inicio.dado:
                nodo.proximo = self.inicio
                self.inicio.anterior = nodo
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.proximo
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.anterior = ant # também poderia ser: nodo.anterior = aux.anterior
                        nodo.proximo = aux
                        ant.proximo = nodo
                        aux.anterior = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.proximo
                if aux == None:
                    ant.proximo = nodo
                    nodo.anterior = ant
                    self.fim = nodo
        self.imprimir()