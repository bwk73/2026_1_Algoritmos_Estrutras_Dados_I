from pythonProject.Questao_Pratica01.Veiculo import Veiculo

class Drone(Veiculo):
    def __init__(self, __helices = 0):
        super().__init__(self, marca = None, modelo = None, prox = None)
        self.__helices = __helices

    def __str__(self):
        txt = f"Quantidade de hélices {self.getHelices()}"
        return super().__str__(txt)

    def getHelices(self):
        return self.__helices

    def setHelices(self, valor):
        if valor != 0:
            self.__helices = valor