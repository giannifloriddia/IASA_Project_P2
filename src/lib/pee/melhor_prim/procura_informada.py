from abc import ABC, abstractmethod
from pee.mec_proc.procura_melh_prim import ProcuraMelhorPrim

class ProcuraInformada(ProcuraMelhorPrim):
    
    def procurar(self, problema, heuristica):
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)