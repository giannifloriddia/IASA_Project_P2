"""
se existir alvo retorna relaçao inversa da distancia
se não existir alvo retorna 0
gama entre ]0,1[ levantado a distancia
"""
from sae import Elemento
from ecr.estimulo import Estimulo

class EstimuloAlvo(Estimulo):

    def __init__(self, direcao, gama = 0.9):
        self.__direcao = direcao
        self.__gama = gama
        
    def detetar(self, percecao):
        #elemento, distancia, _ = percecao[self.__direcao]
        elemento, distancia, _ = percecao.__getitem__(self.__direcao)
        intensidade = self.__gama ** distancia if elemento == Elemento.ALVO else 0
        return intensidade