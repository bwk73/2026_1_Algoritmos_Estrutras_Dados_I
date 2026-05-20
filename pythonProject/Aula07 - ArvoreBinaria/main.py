from Arvore import Arvore

a = Arvore()

a.inserir(a.raiz, 50)
a.inserir(a.raiz, 60)
a.inserir(a.raiz, 40)
a.inserir(a.raiz, 5)
a.inserir(a.raiz, 55)

a.imprimir(a.raiz)
print("\n")
print(a.raiz.dado)
print(a.raiz.esq.dado)
print(a.raiz.dir.dado)
print(a.raiz.esq.esq.dado)
print(a.raiz.dir.esq.dado)
print("\n")
a.imprimirPreOrdem(a.raiz)