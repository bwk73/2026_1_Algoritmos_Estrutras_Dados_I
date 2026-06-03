# estrutura de dados de cada carro da minha fila:
class Carro:
    def __init__(self, modelo = None, placa = None, ano = 2026):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.prox = None

    '''ATENÇÂO: se um método __str__() não for implementado, será retornado o nome da classe
    e o enderço de memória onde está o objeto.'''

    def __str__(self):
        txt = "\nModelo: " + self.modelo
        txt += "\nPlaca: " + self.placa
        txt += "\nAno: " + str(self.placa)
        return txt