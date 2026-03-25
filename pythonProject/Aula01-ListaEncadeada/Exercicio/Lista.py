from No import No

class Lista:
    def __init__(self):
        self.inicio = None

    def imprimir(self):
        print("------------------------------")
        print("Lista Encadeada em ordem crescente (alfabética):")
        if self.inicio is None:
            print("Lista vazia!!!")
        else:
            aux = self.inicio
            while aux:
                print(aux.dado)
                aux = aux.prox
        print("------------------------------")

    # metodo que adiciona em ordem crescente
    def add(self, valor):
        nodo = No(valor) # nodo recebe o endereço de memória
        if self.inicio == None:
            self.inicio = nodo
        else: # dado que acabou de chegar é menor do que o início
            if nodo.dado < self.inicio.dado: # nodo.dado == valor
                nodo.prox = self.inicio
                self.inicio = nodo
            else:
                ant = self.inicio
                aux = self.inicio.prox
                while aux:
                    if nodo.dado < aux.dado:
                        nodo.prox = aux
                        ant.prox = nodo
                        break
                    else:
                        ant = aux
                        aux = aux.prox
                if aux == None:
                    ant.prox = nodo

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