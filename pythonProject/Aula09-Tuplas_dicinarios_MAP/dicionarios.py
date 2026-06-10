carro01 = {"modelo" : "Uno", "ano" : 2004}
carro02 = {"modelo" : "Doblo", "ano" : 2006}
carro03 = {"modelo" : "Renegade", "ano" : 2021}

carro03["motor"] = 1.8

print(carro03)
print(carro02["modelo"])
carro03["modelo"] = "Toro"
del carro03["motor"]
print(carro03)

frota = carro01, carro02
print(frota)
print(frota[1])

# frota[1] = carro03 -> dá erro porque não é possível alterar só uma parte da coleção
# frota = carro01, carro03 -> dá certo porque refaz toda a coleção

# dá certo porque altera o valor de uma posição dentro de um dicionario, que está dentro de uma tupla:
carro02["modelo"] = "Onix"
print("-------------------------------------------------------------------")
print(frota)
