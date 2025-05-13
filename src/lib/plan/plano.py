from plan.planeador import Planeador
from abc import ABC, abstractmethod

class Plano(ABC):

    @abstractmethod
    def obter_acao(self, estado):
        """
        retorna um operador
        """

    @abstractmethod
    def mostrar(self, vista):
        """
        retorna uma vista
        """