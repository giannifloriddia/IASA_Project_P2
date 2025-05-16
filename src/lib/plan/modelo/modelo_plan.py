from abc import ABC, abstractmethod

#Interface para o modelo de planejamento
class ModeloPlan(ABC):

    @abstractmethod
    def obter_estado(self):
        """
        Retorna o estado atual do modelo.
        """
    
    @abstractmethod
    def obter_estados(self):
        """
        Retorna todos os estados do modelo.
        """
    
    @abstractmethod
    def obter_operadores(self):
        """
        Retorna todos os operadores do modelo.
        """