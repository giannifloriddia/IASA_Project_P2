from ecr.reacao import Reacao
from .estimuloObst import EstimuloObst
from .respostaEvitar import RespostaEvitar

"""
Classe que representa a reação de evitar um obstáculo numa determinada direcção.
Esta reação é activada quando o agente detecta um obstáculo na direcção especificada.
"""
class EvitarDir(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloObst(direcao), RespostaEvitar(direcao))