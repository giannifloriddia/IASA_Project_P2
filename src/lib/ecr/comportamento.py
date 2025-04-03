from abc import ABC, abstractmethod

"""
Um comportamento é uma modularização de conjuntos de reacções relacionadas,
realiza de forma modular e coesa o encapsulamento das reacções internas.

TIPOS DE COMPORTAMENTO
• REACÇÃO (comportamento simples)
• COMPORTAMENTO COMPOSTO

Interface Comportamento, usamos uma classe abstrata,
pois o python não suporta interfaces. Usamos
assim a biblioteca abc para garantir que todas
as classes que a implementem tenham o método ativar.
"""
class Comportamento(ABC):
    @abstractmethod
    def ativar(self, percecao):
        """Ativa o comportamento de acordo com a perceção. Retorna acao"""