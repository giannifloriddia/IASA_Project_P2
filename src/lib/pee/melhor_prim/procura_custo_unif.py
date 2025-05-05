from .procura_melh_prim import ProcuraMelhorPrim
from .aval.aval_custo_unif import AvaliadorCustoUnif

"""
A Procura de Custo Uniforme é um caso especial da procura melhor-primeiro, 
onde a função f(n) representa apenas o custo acumulado desde o estado inicial 
até ao nó n. Assim, a estratégia consiste em explorar primeiro os caminhos com menor 
custo total.
Sendo assim, a procura de custo uniforme é ótima e completa,
pois chega sempre ao nó objetivo com o menor custo total, porém tem uma complexidade
computacional elevada.
"""
class ProcuraCustoUnif(ProcuraMelhorPrim):
    
    """
    Inicializa a procura com o super, dando como 
    parâmetro o avaliador de custo uniforme.
    """
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())

    """
    Adicionado por conveniência nos prints.
    """
    def __repr__(self):
        return "Procura Custo Uniforme"