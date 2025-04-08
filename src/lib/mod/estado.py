from abc import ABC, abstractmethod

"""
Um estado representa uma configuração de um sistema ou problema.
Tem de ter uma identificação única.
"""
class Estado(ABC):

    """
    Vamos implementar o método que dá
    um id para o estado, dependendo do problema.
    O id é um número inteiro que representa o estado.
    """
    @abstractmethod
    def id_valor(self):
        """
        Retorna o valor do estado.
        Retorna int.
        """

    """
    Vamos alterar a identificação única do objeto,
    pois queremos que o hash seja o mesmo para dois estados iguais.
    """
    def __hash__(self):
        return self.id_valor()
    
    """
    Como estamos a alterar o hash, também temos de alterar o método de comparação.
    O método __eq__ compara o hash dos dois estados (se forem ambos estados).
    Se o hash for igual, os estados são iguais.
    """
    def __eq__(self, other):
        if isinstance(other, Estado):
            return self.__hash__() == other.__hash__()