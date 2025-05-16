from abc import ABC, abstractmethod
"""
Interface para o planeador
O Planeador é responsável por gerar planos 
a partir de um modelo de planejamento e objetivos.
"""
class Planeador(ABC):
    
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Retorna um plano
        """