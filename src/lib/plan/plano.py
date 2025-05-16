from abc import ABC, abstractmethod

"""
Um plano mantêm a informação dos passos do plano, permitindo obter a
acção a realizar em cada estado do agente (representada por um operador)
"""
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