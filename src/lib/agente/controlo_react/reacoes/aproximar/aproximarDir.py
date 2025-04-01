from ecr.reacao import Reacao
from .estimuloAlvo import EstimuloAlvo
from ..resposta.respostaMover import RespostaMover

class AproximarDir(Reacao):

    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))
