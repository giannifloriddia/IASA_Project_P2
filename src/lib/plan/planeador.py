from abc import ABC, abstractmethod

class Planeador(ABC):
    
    @abstractmethod
    def planear(self, modelo_plan, objetivos):
        """
        Planeia um plano para o modelo_plan com base nos objetivos fornecidos.
        """