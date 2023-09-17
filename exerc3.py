from EstruturasSimplificadas import *

def exerc3(nome_arq = "in3.txt"):
# Ler a entrada uma linha por vez. Em qualquer momento, após ter lido
# as primeiras 42 linhas, se alguma linha é vazia (isto é, uma string de tamanho zero), 
# então imprima a linha que ocorreu 42 linhas antes dela.
# Por exemplo, se a linha 242 é vazia, seu programa deve imprimir a linha
# 200. Seu programa deve ser implementado de tal maneira que ele nunca
# armazene mais de 43 linhas da entrada, em qualquer momento.

    try:
        arq = open(nome_arq, "r", encoding ="utf-8")
    except IOError:
        print("Erro ao abrir arquivo de entrada.")
        return
    deque = Deque()
    sizeFile = len(arq.readlines())
    linha =""
    ultimaLinha=""

    arq.seek(0,0)
    while(sizeFile > 0):
        linha = arq.readline()
        deque.add_last(linha)
        
        sizeFile -=1
        
        if(linha == "\n"):
            print(deque.items,"\n")

        if(deque.size() > 42):
            deque.remove_first()


    arq.close()

if __name__ == "__main__":
    exerc3()
