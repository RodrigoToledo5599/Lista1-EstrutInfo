from EstruturasSimplificadas import *


def exerc1(nome_arq = "in1.txt"):
    # Leia a entrada de uma linha de cada vez e, em seguida, escreva as 
    # linhas em ordem inversa, de modo que a última linha de entrada 
    # seja impressa primeiro, depois a segunda última linha de entrada, 
    # e assim por diante.


    
    try :
        arq_in = open(nome_arq, "r", encoding="utf-8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    
    
    
    
    
    
    deque = Deque()
    sizeFile = len(arq_in.readlines())
    size = 0

    
    arq_in.seek(0,0)
    while(size < sizeFile):
        deque.add_last(arq_in.readline())
        size += 1

    while(size >0):
        print(deque.remove_last())
        size -= 1
    
    
    arq_in.close()

    
    
    

if __name__ == "__main__":
    exerc1()
