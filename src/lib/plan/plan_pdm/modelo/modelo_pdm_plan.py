from pdm.modelo.modelo_pdm import ModeloPDM
from pdm.pdm import PDM
from plan.modelo.modelo_plan import ModeloPlan

class ModeloPDMPlan(ModeloPlan, ModeloPDM):

    def __init__(self, modelo_plan, objetivos, rmax = 1000):
        self.__modelo_plan = modelo_plan
        self.__objetivos = objetivos
        self.__rmax = rmax

    def obter_estado(self):
        self.__modelo_plan.obter_estado()
    
    def obter_estados(self):
        self.__modelo_plan.obter_estados()
    
    def obter_operadores(self):
        self.__modelo_plan.obter_operadores()

    def S(self):
        return self.obter_estados()

    def A(self, s):
        return self.obter_operadores() if s not in self.__objetivos else []

    def T(self, s, a, sn):
        pass

    def R(self, s, a, sn):
        pass

    def suc(self, s, a):
        pass