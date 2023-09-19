from EstruturasSimplificadas import *

def exerc8(nome_arq = "in8.txt"):
    # Leia toda a entrada uma linha de cada vez e, em seguida, imprimir
    # as linhas pares (começando com a primeira linha, linha 0) seguida pelas linhas ímpares.

    try:
        arq = open(nome_arq, "r")
    except:
        print("Erro ao abrir arquivo de entrada.")
        return
    
    arq.seek(0,0)
    fila = Fila()
    
    for linha in arq:

        if(fila is None):
            ...

        if(len(linha)%2 ==0):
            fila.add(linha.strip())
            print(fila.remove())
        else:
            ...



    arq.close()
    print(fila)

if __name__ == "__main__":
    exerc8()
