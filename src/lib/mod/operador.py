from abc import ABC, abstractmethod

"""
É uma representação de uma ação que pode ser aplicada a um estado.
(Gera a transição de um estado para outro.)
"""
class Operador(ABC):

    @abstractmethod
    def aplicar(self, estado):
        """
        Aplica o estado atual a um novo estado. O novo estado é retornado.
        """
    
    @abstractmethod
    def custo(self, estado, estado_suc):
        """
        Calcula o custo de transitar do estado atual para o estado sucessor.
        O custo é retornado.
        Retorna double.
        """