from .mec_util import MecUtil

"""
Classe PDM (Processo de Decisão de Markov),
onde podemos calcular a política ótima e 
utilidade de um modelo de PDM.
"""
class PDM:

    """
    Inicializamos o modelo e o mecanismo de utilidade
    com os parâmetros necessários.
    """
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__mec_util = MecUtil(modelo, gama, delta_max)

    """
    A política representa a estratégia ótima de 
    decisão de um agente num ambiente, ou seja, 
    indica qual a melhor ação a tomar em cada estado, 
    com base nas utilidades calculadas.
    A política é calculada através da maximização
    da utilidade de cada ação em cada estado.
    """
    def politica(self, utilidade):
        S, A, util_acao = self.__modelo.S, self.__modelo.A, self.__mec_util.util_acao
        pol = {}
        for s in S():
            if A(s):
                pol[s] = max(A(s), key=lambda a: util_acao(s, a, utilidade))
        return pol

    """
    O método resolver calcula a utilidade
    e a política do modelo e retorna ambos.
    """
    def resolver(self):
        utilidade = self.__mec_util.utilidade()
        politica = self.politica(utilidade)
        return utilidade, politica