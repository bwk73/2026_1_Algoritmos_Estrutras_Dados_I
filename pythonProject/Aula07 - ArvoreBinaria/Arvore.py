from No import No

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, raiz : No, valor):
        if raiz is None:         # se não tem raiz
            nodo = No(valor)     # crie um nó
            if self.raiz is None:
             self.raiz = nodo     # a raiz recebe o nó
            return nodo

        if valor < raiz.dado:
            raiz.esq = self.inserir(raiz.esq, valor)

        if valor > raiz.dado:
            raiz.dir = self.inserir(raiz.dir, valor)
        return raiz

    def imprimir(self, raiz : No):
        if raiz is not None:
            self.imprimir(raiz.esq)
            print(raiz.dado, end = " - ")
            self.imprimir(raiz.dir)

    def imprimirPreOrdem(self, raiz : No):
        if raiz is not None:
            print(raiz.dado, end = " - ")
            self.imprimir(raiz.esq)
            self.imprimir(raiz.dir)