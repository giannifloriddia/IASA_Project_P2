from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.agente.agente import Agente

class AgenteDelib(Agente):
    def __init__(self):
        super().__init__()
        self.__controlo = ControloDelib(PlaneadorPee())

    def executar(self):
        percecao = self._percepcionar()
        acao = self.__controlo.processar(percecao)
        self.__controlo.mostrar(self.vista)
        self._actuar(acao)