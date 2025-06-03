from plan.plan_pdm.modelo.modelo_pdm_plan import ModeloPDMPlan
from plan.planeador import Planeador
from pdm.pdm import PDM
from plan.plan_pdm.plano_pdm import PlanoPDM

"""
O PlaneadorPDM é responsável por planear ações
utilizando o modelo de decisão de Markov (PDM).
Usamos como valores defaults o gama a 0.85 e o delta_max a 1.
"""
class PlaneadorPDM(Planeador):

    def __init__(self, gama = 0.85, delta_max = 1):
        self.__gama = gama
        self.__delta_max = delta_max

    def planear(self, modelo_plan, objetivos):
        modelo_pdm = ModeloPDMPlan(modelo_plan, objetivos)
        pdm = PDM(modelo_pdm, self.__gama, self.__delta_max)
        utilidade, politica = pdm.resolver()
        return PlanoPDM(utilidade, politica)