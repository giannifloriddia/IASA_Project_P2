from pdm.pdm import PDM
from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.plan_pdm.plano_pdm import PlanoPDM
from plan.planeador import Planeador

class PlaneadorPDM(Planeador):

    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plano, objetivos):
        modelo = ModeloPDMPlan(modelo_plano, objetivos)
        pdm = PDM(modelo, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)