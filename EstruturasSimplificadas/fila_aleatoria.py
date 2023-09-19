from .fila import Fila
from random import randrange

class FilaAleatoria(Fila):
    # escreva o método remove que remove um elemento aleatório da fila
    # fique atento, pois se você remover diretamente um elemento aleatório
    # sua implementação será O(n), onde n é o tamanho da fila.
    # Você deve implementar este método de forma que ele seja O(1).

    def remove(self):
        r = randrange(0,self.size())
        
        variable = self.fila.pop(r)
        return variable
