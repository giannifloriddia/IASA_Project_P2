from sae import Agente
from .controlo_react.controlo_react import ControloReact
from .controlo_react.reacoes.recolher import Recolher
from sae.agente.accao import Accao

"""
Classe que implementa um agente reativo simples
tem como atributos um controlo reativo,
neste caso foi usado somentente o comportamento de explorar
para efeitos de teste. 
"""
class AgenteReact(Agente):
    def __init__(self):
        super().__init__()
        self.__controlo = ControloReact(Recolher())

    """
    Método igual ao método implementado em Java,
    chama os metodos percepcionar, processar e atuar
    e que não devolve nada. Este metodo chama o metodo percepcionar,
    que retorna uma percepção, chama o metodo processar do controlo, 
    que recebe a percepção e devolve uma ação,
    e chama o metodo atuar, que executa o comando da ação no ambiente.
    """
    def executar(self):
        percecao = self._percepcionar()
        acao = self.__controlo.processar(percecao)
        self._actuar(acao)