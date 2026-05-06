class Veiculo:
    def __init__(self, marca = None, modelo = None, prox = None):
        self.marca = marca
        self.modelo = modelo
        self.prox = prox

    def __str__(self):
        txt = "### Veículo  ###"
        txt += f"\nMarca: {self.marca}"
        txt += f"\nModelo: {self.modelo} "
        return txt