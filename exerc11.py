from EstruturasSimplificadas import *
from random import randint

def exerc11():
    # Suponha que você tenha uma Pilha, s, que suporta somente as operações
    # push(x) e pop(). Mostre como, usando somente uma fila FIFO, f, você
    # pode reverter a ordem de todos os elementos em s.

    s = Pilha()
    for i in range(40):
        s.push(i)

    while s.size() > 1:
        print(s.pop())
    

   
   
if __name__ == "__main__":
    exerc11()
