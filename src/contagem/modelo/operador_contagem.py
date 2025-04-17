from .estado_contagem import EstadoContagem
from mod.operador import Operador

"""
Neste problema, o operador é o incremento.
O operador é responsável por incrementar o valor atual do estado.
Portanto, adicionamos um parâmetro ao operador, que é o incremento.
O operador também tem um custo, que neste caso, 
definimos como o quadrado do incremento.
"""
class OperadorIncremento(Operador):

    def __init__(self, incremento):
        self.incremento = incremento

    """
    O operador aplica o incremento ao estado atual e retorna o novo estado.
    O novo estado é o estado atual + incremento.
    """
    def aplicar(self, estado):
        return EstadoContagem(estado.valor + self.incremento)

    """
    Neste caso, não utilizamos o estado e o estado sucessor
    para calcular o custo, mas em outros problemas,
    é comum utilizar o estado atual e o estado sucessor para calcular o custo.
    """
    def custo(self, estado, estadoSucessor):
        return self.incremento**2