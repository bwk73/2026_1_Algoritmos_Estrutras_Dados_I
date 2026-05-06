from pythonProject.Questao_Pratica01.Veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, _portas = 0):
        super().__init__(self, marca = None, modelo = None, prox = None)
        self._portas = _portas

    def __str__(self):
        txt = f"Número de portas: {self.getPortas()}"
        return super().__str__(txt)

    def getPortas(self):
         return self._portas

    def setHelices(self, valor):
         if valor != 0:
            self._portas = valor