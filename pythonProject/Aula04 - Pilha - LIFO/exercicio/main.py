from Livro import Livro
from Autor import Autor
from Pilha import Pilha

lifo = Pilha()
lifo.imprimir()

a1 = Autor("Machado de Assis", 1839)
a2 = Autor("Érico Veríssimo", 1905)

l1 = Livro("Dom Casmurro", 288, a1)
l2 = Livro("O Tempo e o Vento", 2832, a2)
l3 = Livro("Viva a Vida")
l4 = Livro("Memórias Póstumas de Brás Cubas", 285, a1)

lifo.add(l1)
lifo.add(l3)
lifo.add(l2)
lifo.remover()
lifo.add(l4)

lifo.contLivrosPorAutor("Adalto")
lifo.contLivrosPorAutor("Machado de Assis")