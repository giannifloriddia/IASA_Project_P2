from ecr.resposta import Resposta
from sae.agente.accao import Accao

"""
Esta classe é responsável por criar uma resposta 
de movimento com base na direção fornecida.
"""
class RespostaMover(Resposta):

    def __init__(self, direcao):
        self._direcao = direcao
        acao = Accao(direcao)
        super().__init__(acao)

