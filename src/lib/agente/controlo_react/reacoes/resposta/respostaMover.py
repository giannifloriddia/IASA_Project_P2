from ecr.resposta import Resposta
from sae.agente.accao import Accao

class RespostaMover(Resposta):

    def _init_(self, direcao):
        self.__direcao = direcao
        acao = Accao(self.__direcao)
        super()._init_(acao)

