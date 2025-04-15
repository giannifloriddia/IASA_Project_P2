from mod.problema import Problema
from .operador_contagem import OperadorIncremento
from .estado_contagem import EstadoContagem

class ProblemaContagem(Problema):
    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(incremento) for incremento in incrementos])
        self.__valor_final = valor_final

    def objetivo(self, estado):
        return estado.valor >= self.__valor_final