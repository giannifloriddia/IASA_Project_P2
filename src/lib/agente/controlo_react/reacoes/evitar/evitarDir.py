from ecr.reacao import Reacao
from ..estimuloObst import EstimuloObst

class EvitarDir(Reacao):
    def __init__(self, direcao):
        super().__init__(EstimuloObst(direcao), None)