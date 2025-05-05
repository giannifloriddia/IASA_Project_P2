from abc import ABC, abstractmethod

"""
Um avaliador é uma classe que avalia a prioridade de um nó em uma árvore de busca.
Ele é usado para determinar a ordem em que os nós devem ser explorados.
(Define o contrato funcional (interface) de avaliação da prioridade de um nó para
ordenação da fronteira por prioridade, é concretizado de acordo o tipo de procura.)
"""
class Avaliador(ABC):

    @abstractmethod
    def prioridade(self, no):
        """retorna a prioridade do nó"""