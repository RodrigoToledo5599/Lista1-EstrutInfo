from EstruturasSimplificadas import *

def exerc2(nome_arq = 'in2.txt'):
   # Ler as primeiras 50 linhas de uma entrada e então escrevê-las na ordem
   # reversa. Ler as próximas 50 linhas e então escrevê-las em ordem reversa.
   # Fazer isso até que não existam mais linhas a serem lidas, neste ponto as
   # linhas restantes devem ser impressas em ordem reversa.
   # Em outras palavras, sua saída vai começar com a linha de número 50,
   # então a 49, 48 e assim por diante até a primeira linha. Isso será seguido
   # pela linha de número 100, seguida pela 99 98 até a linha 51, e assim por diante.
   # Seu código nunca deverá ter armazenado mais de 50 linhas.

    try:
        arq = open(nome_arq, "r" ,encoding="utf-8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return

    

    sizeFile = len(arq.readlines())
    sizeAtual = sizeFile
    pilha = Pilha()
    
    arq.seek(0,0)
    for i in range(sizeFile):
        pilha.push(arq.readline())
        sizeAtual -= 1
        
        if(pilha.size() == 50 or sizeAtual == 0):
            for i in range(50):
                print(pilha.pop())


    
    arq.close()

if __name__ == "__main__":
    exerc2()
