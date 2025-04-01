from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar

class ExplorarComMemoria(Comportamento):
    def __init__(self, size = 100):
        self.__memoria = []
        self.__size = size
    
    def ativar(self, percecao):
        situacao = percecao.posicao, percecao.direccao
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            if len(self.__memoria) > self.__size:
                self.__memoria.pop(0)
            return Avancar()
