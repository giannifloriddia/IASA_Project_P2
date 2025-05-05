from abc import ABC

"""
O avaliador heurístico é uma classe abstrata utilizada para 
armazenar a heurística que será utilizada na procura informada.
"""
class AvaliadorHeur(ABC):

    #read
    @property
    def heuristica(self):
        return self._heuristica
    
    #write
    @heuristica.setter
    def heuristica(self, heuristica):
        self._heuristica = heuristica
    
    def __init__(self):
        self._heuristica = None