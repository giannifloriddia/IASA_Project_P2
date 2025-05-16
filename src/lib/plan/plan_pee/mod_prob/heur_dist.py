import math
from pee.melhor_prim.aval.heuristica import Heuristica

"""
Neste caso precisamos de guardar o estado final para
calcular a heurística, que irá ser a distância entre a
posição do estado atual e a posição do estado final.
"""
class HeurDist(Heuristica):
    
    def __init__(self, estado_final):
        self.__estado_final = estado_final

    def h(self, estado):
        return math.dist(estado.posicao, self.__estado_final.posicao)