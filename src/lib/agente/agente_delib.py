from agente.controlo_delib.controlo_delib import ControloDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.agente.agente import Agente

"""
A classe AgenteDelib representa um agente deliberativo, capaz de 
planear ações com base numa representação interna do ambiente. Diferente 
dos agentes reativos, este tipo de agente antecipa o futuro através 
de raciocínio e tomada de decisão, utilizando a memória para simular 
e escolher a melhor ação a tomar. O agente usa um controlador 
com um planeador para processar perceções, gerar planos e atuar, 
tornando o seu comportamento mais inteligente e otimizado.
"""
class AgenteDelib(Agente):
    def __init__(self):
        super().__init__()
        self.__controlo = ControloDelib(PlaneadorPee())

    """
    Executar é percecionar o ambiente, processar 
    a perceção e atuar de acordo com a ação.
    """
    def executar(self):
        percecao = self._percepcionar()
        acao = self.__controlo.processar(percecao)
        self.__controlo.mostrar(self.vista)
        self._actuar(acao)