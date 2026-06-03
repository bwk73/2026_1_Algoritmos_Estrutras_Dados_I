'''Exercício para 08/04/2026: implemente uma fila de carros de um lava jato.
Cada carro deve conter um modelo, placa e ano. Implemente um método para adicionar
 carro na fila, um método para lavar um carro e um método para iprimir a fila de carros.'''
from Fila import Fila
from Carro import Carro

fila = Fila()

op = -1
while op != 0:
    print("1) Adicionar Carro")
    print("2) Imprimir Fila")
    print("3) Lavar Carro")
    print("0) Sair")
    op = int(input("Digite sua opção: "))

    if op == 1:
        carro = Carro()
        carro.modelo = input("Modelo: ")
        carro.placa = input("Placa: ")
        carro.ano = int(input("Ano: "))
        fila.add(carro)
    if op == 2:
        fila.imprimir()
    if op == 3:
        fila.lavar()
    if op == 0:
        print("Tchau!!!")
    if op >3 or op < 0:
        print("Opção inválida!!!")