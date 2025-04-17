from mod.problema import Problema
from .operador_contagem import OperadorIncremento
from .estado_contagem import EstadoContagem

"""
Criamos a classe ProblemaContagem, que herda da classe Problema.
A classe possui um método objetivo que verifica 
se o estado atual atingiu o valor final.
No construtor, temos de inserir o valor inicial,
o valor final e os incrementos.
O valor inicial é o ponto de partida da contagem,
o valor final é o objetivo a ser alcançado e os incrementos
são os passos que podemos dar na contagem, que irão ser uma 
lista de operadores.
"""
class ProblemaContagem(Problema):

    def __init__(self, valor_inicial, valor_final, incrementos):
        super().__init__(EstadoContagem(valor_inicial), [OperadorIncremento(incremento) for incremento in incrementos])
        self.__valor_final = valor_final

    """
    Neste problema, chegamos ao objetivo quando o valor do estado
    for maior ou igual ao valor final.
    """
    def objetivo(self, estado):
        return estado.valor >= self.__valor_final