class Torre:
    def __init__(self, id = 0, nome = None, endereco = None):
        self.id = id
        self.nome = nome
        self.endereco = endereco

    def __str__(self):
        return  f"""Torre: {self.id} - {self.nome}
                    Endereço: {self.endereco}"""

    def imprimir(self):
        print(self)