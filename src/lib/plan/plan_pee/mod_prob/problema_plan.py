from mod.problema import Problema

"""
Classe que define o nosso problema especifico. 
"""
class ProblemaPlan(Problema):
    
    """
    Chama o super construtor da classe Problema, passando o estado
    inicial e os operadores do modelo de planeamento, e inicializa
    o estado final.
    """
    def __init__(self, modelo_plan, estado_final):
        super().__init__(modelo_plan.obter_estado(), modelo_plan.obter_operadores())
        self.__estado_final = estado_final

    """
    Retorna se o estado é o objetivo final do problema
    """
    def objetivo(self, estado):
        return estado == self.__estado_final