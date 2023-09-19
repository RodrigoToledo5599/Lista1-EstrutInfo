from EstruturasSimplificadas import *

def exerc10(String):
    # Uma String casada é uma sequência de caracteres {, }, (, ), [, e ] que
    # estejam casados corretamente. Por exemplo, {{()[]}} é uma String
    # casada, porém {{()]} não é, pois o segundo { casa com um ]. Mostre
    # que uma pilha pode ser usada para isso de tal modo que dada uma String
    # de tamanho n, você possa determinar se ela é uma String casada no tempo O(n).
    
    # Escreva aqui sua resposta para o exercício 10. Sua resposta deve retornar 
    # True ou False de acordo com o resultado do casamento da String.
    
    ChavesAbertura = 0
    ColchetesAbertura = 0
    ParentesesAbertura = 0

    ChavesFechamento = 0
    ColchetesFechamento = 0
    ParentesesFechamento = 0

    String = str(input("Digite a sua string:\t"))

    for i in range(len(String)):
        if(String[i] =="{"):
            ChavesAbertura +=1
        elif(String[i] == "}"):
            ChavesFechamento +=1
        elif(String[i] == "["):
            ColchetesAbertura +=1
        elif(String[i] == "]"):
            ColchetesFechamento +=1
        elif(String[i] == "("):
            ParentesesAbertura +=1
        elif(String[i] == ")"):
            ParentesesFechamento +=1

    if(ChavesAbertura == ChavesFechamento):
        print("casada")

    elif(ChavesAbertura == ChavesFechamento and ParentesesAbertura == ParentesesFechamento):
        print("casada")

    elif(ChavesAbertura == ChavesFechamento and ParentesesAbertura == ParentesesFechamento and ColchetesAbertura == ChavesFechamento):
        print("casada")
        
    else:
        print("nao casada")



    

if __name__ == "__main__":
    exerc10("{{()[]}") # Não é uma String casada
    exerc10("{{()[]}}") # É uma string casada
    exerc10("{{()]}") # Não é uma string casada
    exerc10("{{()[]}}{") # Não é uma string casada
    exerc10("{{()[]}}{}") # É uma string casada
    exerc10("{{()[]}}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{") # Não é uma string casada
    exerc10("{{()[]}}{}{}{}") # É uma string casada
    exerc10("{{()[]}}{}{}{}{") # Não é uma string casada
    exerc10("") # É uma string casada
