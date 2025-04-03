from ecr.comportamento import Comportamento
import random
from sae import Avancar, Rodar, Direccao

"""
Explorar é um comportamento simples pois
não tem nem estímulos nem respostas associadas.
O comportamento é simplesmente escolher
aleatoriamente entre avançar e rodar numa
direção aleatória. 
A probabilidade de rodar é  iniciada a 70%.
Dentro do rodar é escolhida uma direção aleatória.
"""
class Explorar(Comportamento):

    def __init__(self, probabilidade=0.7):
        super().__init__()
        self.__probabilidade = probabilidade
        self.__direcoes = list(Direccao)
    
    #Ignoramos a perceção pois não é relevante para este comportamento
    def ativar(self, percecao):
        acao = None
        probs = random.random()
        if probs >= self.__probabilidade:
            acao = Avancar()
        else:
            acao = Rodar(random.choice(self.__direcoes))
        return acao