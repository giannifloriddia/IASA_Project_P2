from abc import ABC, abstractmethod

"""
Uma fronteira é uma coleção de nós que estão prontos para serem expandidos.
Tem de ter métodos para inserir e remover nós.
Uma fronteira pode estar vazia ou não, se estiver vazia,
é porque chegámos ao final da árvore, ou porque estamos no primeiro elemento da árvore.
"""
class Fronteira(ABC):

    @property
    def vazia(self):
        return self.__vazia

    def __init__(self):
        self.__vazia = True
        self._nos = []

    def iniciar(self):
        pass

    @abstractmethod
    def inserir(self, no):
        pass

    def remover(self):
        pass