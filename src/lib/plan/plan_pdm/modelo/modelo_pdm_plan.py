from pdm.modelo.modelo_pdm import ModeloPDM
from plan.modelo.modelo_plan import ModeloPlan

"""
Criamos o ModeloPDMPlan que implementa duas interfaces:
- ModeloPlan: para obter os estados, operadores e transições
- ModeloPDM: para obter os estados, ações, transições e recompensas
Isto permite que o modelo seja utilizado com o PDM (Processo de Decisão de Markov)
e que possa ser usado para planear ações com base num modelo de decisão.
"""
class ModeloPDMPlan(ModeloPlan, ModeloPDM):

    def __init__(self, modelo_plan, objetivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax
        #Gera todas as transições inicialmente
        #para não ser calculado milhares de vezes
        #quando corre o programa
        self.__transicoes = {}
        #Utizamos operadores para simular as ações
        for s in self.obter_estados():
            for a in self.obter_operadores():
                sn = a.aplicar(s)
                if sn:
                    self.__transicoes[(s, a)] = sn

    #Utilizamos uma função em ordem da outra por redundância
    def obter_estado(self):
        return self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        return self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        return self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()

    def A(self, s):
        return self.obter_operadores() if s not in self.__objetivos else []

    def T(self, s, a, sn):
        sn = self.__transicoes.get((s, a))
        #is not None não seria necessário neste caso, mas é mais explícito
        return 1 if sn is not None else 0

    """
    A recompensa máxima é atribuída somente quando o estado sucessor
    é um dos estados terminais (objetivos).
    """
    def R(self, s, a, sn):
        return self.__rmax if sn in self.__objetivos else 0

    def suc(self, s, a):
        sn = self.__transicoes.get((s, a))
        #retornamos uma lista porque se for não determinsta pode haver mais do que um estado sucessor
        return [sn] if sn is not None else []