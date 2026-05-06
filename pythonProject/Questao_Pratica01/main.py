from Carro import Carro
from Drone import Drone
from PilhaCarros import PilhaCarros
from PilhaDrones import PilhaDrones
from pythonProject.Questao_Pratica01.PilhaCarros import printCarro
from pythonProject.Questao_Pratica01.PilhaDrones import printDrone

c1 = Carro()
c2 = Carro()
c3 = Carro()

d1 = Drone()
d2 = Drone()
d3 = Drone()

pc = PilhaCarros()
pd = PilhaDrones()

op = -1

def menu():
    print("-----------------------------")
    print("| 1) Adicionar Carro | ")
    print("| 2) Remover Carro | ")
    print("| 3) Imprimir Pilha de Carros | ")
    print("| 4) Adicionar Drone | ")
    print("| 5) Remover Drone | ")
    print("| 6) Imprimir Pilha de Drones | ")
    print("| 0) Sair                  | ")
    print("-----------------------------")

def adicionarCarro():
    marca = int(input("Marca do carro: "))
    modelo = input("Modelo do carro: ")
    novoCarro = Carro(marca, modelo, c1)
    pc.addCarro(novoCarro)

def removerCarro():
     pc.remCarro()

def adicionarDrone():
    marca = int(input("Marca do drone: "))
    modelo = input("Modelo do drone: ")
    novoDrone = Carro(marca, modelo, d1)
    pd.addDrone(novoDrone)

def removerDrone():
    pd.remDrone

while op != 0:
    menu()
    op = int(input("Digite sua opção: "))
    if op == 1:
        adicionarCarro()
    if op == 2:
        removerCarro()
    if op == 3:
        printCarro().imprimir()
    if op == 4:
        adicionarDrone()
    if op == 5:
        removerDrone()
    if op == 6:
        printDrone().imprimir()
    if op < 0 or op > 6:
        print("Opção inválida!")
    if op == 0:
        print("Tchau!")