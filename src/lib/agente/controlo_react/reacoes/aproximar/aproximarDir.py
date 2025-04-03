from ecr.reacao import Reacao
from .estimuloAlvo import EstimuloAlvo
from ..resposta.respostaMover import RespostaMover

"""
Módulo que implementa a reação AproximarDir, 
que aproxima o agente de um alvo numa direção específica.
A reação é ativada quando o agente detecta um alvo na direção especificada. 
A resposta do agente é mover-se nessa direção.
"""
class AproximarDir(Reacao):

    def __init__(self, direcao):
        super().__init__(EstimuloAlvo(direcao), RespostaMover(direcao))
