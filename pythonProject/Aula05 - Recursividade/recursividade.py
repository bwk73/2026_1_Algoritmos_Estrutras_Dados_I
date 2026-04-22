def somarAte(n):
    if n == 1:
        return 1
    else:
        return n + somarAte(n-1)

print("Soma de 1 até 3: ", somarAte(3))
print("Soma de 1 até 5: ", somarAte(5))

'''fatorial de 5:
5! = 5 * 4 * 3 * 2 * 1 = 120
'''
def fatorial(x):
    if x == 0:
        return 1
    else:
        return x * fatorial(x - 1)

print("Fatorial de 5 é: ", fatorial(5))

# 1) Implemente uma função recursiva para cálculo de potência:
def potencia(base, expoente):
    if expoente == 0:
        return 1
    else:
        return base * potencia(base, expoente - 1)

print("Potência de base 2 elevada à potência 5: ", potencia(2, 5))

# 2) Implemente uma função recursiva para contagem regressiva:
import time
def contagemRegressiva(x):
   time.sleep(1)
   if x == 0:
       print("Fim")
   else:
       print(x)
       contagemRegressiva(x - 1)

print(contagemRegressiva(5))

# 3) Implemente uma função recursiva para inverter uma string:
def inverterString(s):
    if len(s) <= 1:
        return s
    return inverterString(s[1:]) + s[0]

print(inverterString("Benjamin"))