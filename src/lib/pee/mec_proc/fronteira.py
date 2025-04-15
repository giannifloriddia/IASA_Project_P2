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
        return len(self._nos) == 0

    def __init__(self):
        self.iniciar()

    def iniciar(self):
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """ Insere um nó na fronteira. """

    def remover(self):
        return self._nos.pop(0)