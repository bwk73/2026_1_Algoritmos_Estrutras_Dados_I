""" Construa um algoritmo que possua uma tupla com os números escritos
por extenso de “zero” a “nove”. Peça ao usuário para digitar um número
de 0 a 9 e retorne a ele o número por extenso, sem usar estruturas
condicionais (if e switch). """

def converteNumeros(numeros):
    for n in numeros:
        numeros[n] = numerosExtenso[n]

numeros = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
numerosExtenso = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove")
num = int(input("Digite um número de 0 à nove: "))
print(list(map(converteNumeros, num)))
