from ecr.reacao import Reacao
from .estimuloObst import EstimuloObst
from .respostaEvitar import RespostaEvitar

class EvitarDir(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloObst(direcao), RespostaEvitar(direcao))