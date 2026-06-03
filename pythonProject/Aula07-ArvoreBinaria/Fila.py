from No import No
from NoFila import NoFila
# A fila é só um meio de percorrer a árvore em nível.
class Fila:
    def __init__(self):
        self.inicio = None
        self.fim = None
        self.tamanho = 0

    def add(self, noArvore: No):
        nodo = NoFila(noArvore)
        if self.inicio is None:
            self.inicio = nodo
        else:
            self.fim.prox = nodo
        self.fim = nodo
        self.tamanho += 1

    def remover(self):  # remove da fila, não da árvore
        if self.inicio is not None:
            aux = self.inicio.noArvore
            self.inicio = self.inicio.prox
            if self.inicio == None:
                self.fim = None
            self.tamanho -= 1
            return aux
        return None