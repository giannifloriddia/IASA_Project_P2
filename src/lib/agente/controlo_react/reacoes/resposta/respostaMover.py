from ecr.resposta import Resposta
from sae.agente.accao import Accao

class RespostaMover(Resposta):

    def __init__(self, direcao):
        self._direcao = direcao
        acao = Accao(direcao)
        super().__init__(acao)

