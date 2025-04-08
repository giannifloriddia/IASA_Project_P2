from sae import Elemento
from ecr.estimulo import Estimulo

"""
Um estimulo que detecta a presença de um alvo na direção dada.
A intensidade do estimulo é dada pela relação inversa da distância ao alvo.
Se existir alvo retorna relaçao inversa da distancia, se não existir alvo retorna 0.
Gama entre ]0,1[ elevado à distancia.
"""
class EstimuloAlvo(Estimulo):

    def __init__(self, direcao, gama = 0.9):
        self.__direcao = direcao
        self.__gama = gama

    """    
    Usa o método __getitem__ para aceder ao tuplo (elemento, distancia, posicao)
    Usamos underscore para ignorar o valor da posicao, pois neste caso não é necessária.
    """
    def detetar(self, percecao):
        #elemento, distancia, _ = percecao[self.__direcao]
        # Vendo a documentação, também pode ser:
        elemento, distancia, _ = percecao.__getitem__(self.__direcao)
        intensidade = self.__gama ** distancia if elemento == Elemento.ALVO else 0
        return intensidade