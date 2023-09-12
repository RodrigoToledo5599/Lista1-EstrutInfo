from EstruturasSimplificadas import *

def exerc10(string):
    # Uma string casada é uma sequência de caracteres {, }, (, ), [, e ] que
    # estejam casados corretamente. Por exemplo, {{()[]}} é uma string
    # casada, porém {{()]} não é, pois o segundo { casa com um ]. Mostre
    # que uma pilha pode ser usada para isso de tal modo que dada uma string
    # de tamanho n, você possa determinar se ela é uma string casada no tempo O(n).
    
    # Escreva aqui sua resposta para o exercício 10. Sua resposta deve retornar 
    # True ou False de acordo com o resultado do casamento da string.
    pass # Apague esta linha

    

if __name__ == "__main__":
    exerc10("{{()[]}") # Não é uma string casada
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
