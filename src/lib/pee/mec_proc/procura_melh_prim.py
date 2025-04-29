from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade
from ..melhor_prim.fronteira_prioridade import FronteiraPrioridade
from .procura_grafo import ProcuraGrafo
from abc import ABC, abstractmethod

class ProcuraMelhorPrim(ProcuraGrafo, ABC):

    def __init__(self, avaliador):
        fronteira = FronteiraPrioridade(avaliador)
        self._avaliador = avaliador
        super().__init__(fronteira)

    def _manter(self, no):
        return no.estado not in self._explorados or no.custo < self._explorados[no.estado].custo