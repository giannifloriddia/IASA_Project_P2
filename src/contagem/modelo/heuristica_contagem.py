from pee.melhor_prim.aval.heuristica import Heuristica

"""
Definimos a heurística de contagem, que neste caso é o valor
absoluto da diferença entre o valor atual e o valor final.
"""
class HeuristicaContagem(Heuristica):
    
    """
    Inicializa a heurística com o valor final desejado.
    """
    def __init__(self, valorfinal):
        self.__valor_final = valorfinal

    def h(self, estado):
        return abs(estado.id_valor() - self.__valor_final)