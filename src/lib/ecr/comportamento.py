from abc import ABC, abstractmethod

"""
Interface Comportamento, usamos uma classe abstrata,
pois o python não suporta interfaces. Usamos
assim a biblioteca abc para garantir que todas
as classes que a implementem tenham o método ativar.
"""
class Comportamento(ABC):
    @abstractmethod
    def ativar(self, percecao):
        """Ativa o comportamento de acordo com a perceção. Retorna acao"""