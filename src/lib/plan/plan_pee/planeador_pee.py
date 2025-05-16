from pee.melhor_prim.procura_aa import ProcuraAA
from plan.plan_pee.mod_prob.heur_dist import HeurDist
from plan.plan_pee.mod_prob.problema_plan import ProblemaPlan
from plan.plan_pee.plano_pee import PlanoPEE
from plan.planeador import Planeador

"""
Gera a solução do plano a partir do modelo de planeamento e dos objetivos.
"""
class PlaneadorPee(Planeador):

    """
    Inicializamos o mecanismo de procura A*.
    """
    def __init__(self):
        self.__mec_pee = ProcuraAA()

    """
    O estado final é o primeiro objetivo da lista de objetivos.
    Crimaos o problema e a heurística, e geramos uma solução
    através do mecansimo de procura A*.
    """
    def planear(self, modelo_plan, objetivos):
        estado_final = objetivos[0]
        problema = ProblemaPlan(modelo_plan, estado_final)
        heuristica = HeurDist(estado_final)
        solucao = self.__mec_pee.procurar(problema, heuristica)
        return PlanoPEE(solucao)