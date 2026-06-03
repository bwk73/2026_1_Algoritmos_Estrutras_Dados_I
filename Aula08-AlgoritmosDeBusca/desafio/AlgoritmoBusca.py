class AlgoritmoBusca:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def buscaSequencial(self):
        pass

    def buscaBinaria(self):
        self.inicio = 0


"""
int buscaBin (int v[], int n, int k)
{
int inicio o = 0 ;              // início do vetor ou de parte do vetor (primeiro elemento)
int fim-n-1;                    // final do vetor ou de parte do vetor (último elemento)
int centro;                     // posição central do vetor
while (inicio <= fim) {         // enquanto existir elementos no vetor...
centro inicio+(fim-inicio)/2;   // recebe a posição central do vetor
if (k == v(centro)) return centro;      // caso (1) - encontrou o valor
else if (k > v[centro])         // caso (2) o valor do elemento central é menor que k
inicio centro+1;                // nesse caso (2) o novo vetor passa a ser a parte superior.
else
}                               // caso (3) - o valor do elemento central é maior que k
fim-centro-1;                   // nesse caso (3) o novo vetor passa a ser a parte inferior.
return -1;                      // caso o valor não seja encontrado, retoma o valor -1
}
"""
