from abc import ABC, abstractmethod

"""
Interface Estimulo, usamos uma classe abstrata,
pois o python não suporta interfaces. Usamos
assim a biblioteca abc para garantir que todas
as classes que a implementem tenham o método
detetar.
"""
class Estimulo(ABC):

    #Forma para criar métodos abstratos
    @abstractmethod
    def detetar(self, percecao):
        """Detetar o estímulo na perceção. Retorna float"""