from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("------------------------------")
        print("Lista Encadeada por ordem de chegada:")
        if self.inicio is None:
            print("Lista vazia!!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.prox
        print("------------------------------")

    # metodo que adiciona por ordem de chegada
    def add(self, valor):
        nodo = No(valor) # nodo recebe o endereço de memória
        if self.inicio == None:
            self.inicio = nodo
        else:
            aux = self.inicio
            while aux.prox:
                aux = aux.prox
            aux.prox = nodo
        self.imprimir()

    def remover(self, valor):   # metodo que remove qualquer elemento de qualquer posição
        if self.inicio == None:
            print("Lista vazia!")
        else:
            removeu = False
            if valor == self.inicio.dado:
                self.inicio = self.inicio.prox
                removeu = True
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if valor == aux.dado:
                        ant.prox = aux.prox
                        removeu = True
                        break
                    else:
                        ant = aux
                        aux = aux.prox
            if removeu:
                print(valor, " removido!!!")
            else:
                print(valor, "não encontrado!!!")

            self.imprimir()