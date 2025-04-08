from abc import ABC, abstractmethod

"""
Um problema é uma representação de um sistema ou situação que queremos resolver.
Um problema tem um estado inicial e uma lista de operadores que podem ser aplicados a esse estado.
Tem também um estado objetivo, que é o estado que queremos alcançar.
"""
class Problema(ABC):

    """
    Definimos as propriedades do problema.
    Usamos o assert para garantir que a lista de operadores não é vazia.
    """
    def __init__(self, estado_inicial, operadores):
        self.__estado_inicial = estado_inicial
        assert len(operadores) >= 1, "Lista de operadores não pode ser vazia."
        self.__operadores = operadores

    @property
    def estado_inicial(self):
        return self.__estado_inicial
    
    @property
    def operadores(self):
        return self.__operadores
    
    @abstractmethod
    def objetivo(self, estado):
        """
        Verifica se o estado é o objetivo.
        Retorna True se for o objetivo, False caso contrário.
        """