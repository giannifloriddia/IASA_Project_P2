from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pdm.planeador_pdm import PlaneadorPDM
from sae.agente.agente import Agente

"""
A classe AgenteDelibPDM representa um agente deliberativo que utiliza
um Planeador PDM (Planeamento por Decisão de Markov) para tomar decisões.
Diferentemente do AgenteDelib, este agente é capaz de lidar com incertezas
e otimizar suas ações com base num modelo do ambiente.
Chamamos a um processo de decisão de Markov (PDM) pois a previsão dos
estados seguintes depende somente do estado presente.

Alteramos o valor do gama para 0.95 (fator de pearmibilidade), para que
o agente possa "ver" mais longe no futuro. Pois se o gama for baixo,
o agente só se preocupa com os estado mais próximos, e não com as consequências
das suas ações a longo prazo.
"""
class AgenteDelibPDM(Agente):
    def __init__(self):
        super().__init__()
        self.__controlo = ControloDelib(PlaneadorPDM(0.95))

    """
    Executar é percecionar o ambiente, processar 
    a perceção e atuar de acordo com a ação.
    """
    def executar(self):
        percecao = self._percepcionar()
        acao = self.__controlo.processar(percecao)
        self.__controlo.mostrar(self.vista)
        self._actuar(acao)