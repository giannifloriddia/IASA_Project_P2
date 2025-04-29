from abc import ABC, abstractmethod

class AvaliadorHeur(ABC):

    @property
    def heuristica(self):
        return self._heuristica
    
    @heuristica.setter
    def heuristica(self, heuristica):
        self._heuristica = heuristica
    
    def __init__(self):
        self._heuristica = None