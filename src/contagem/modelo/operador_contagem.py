from .estado_contagem import EstadoContagem
from mod.operador import Operador

class OperadorIncremento(Operador):
    def __init__(self, incremento):
        self.incremento = incremento

    def aplicar(self, estado):
        EstadoSucessor = EstadoContagem(estado.valor + self.incremento)
        return EstadoSucessor

    def custo(self, estado, estadoSucessor):
        return self.incremento**2