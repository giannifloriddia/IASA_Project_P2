from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

"""
A classe PassoSolucao é uma representação de um passo na solução de um problema,
onde cada passo é composto por um estado e um operador.
A classe PassoSolucao é uma estrutura de dados que armazena o estado atual do problema
e o operador que foi aplicado para chegar a esse estado.

A anotação @dataclass é uma forma de simplificar a criação de classes em Python,
especialmente quando essas classes são usadas para armazenar dados.
A anotação gera automaticamente métodos especiais como __init__, __repr__, __eq__ e outros,
com base nos atributos definidos na classe.

Neste caso, a implementação irá gerar getters e setters, os seja os atributos serão read/write, 
fazendo assim com que a nossa implementação fique diferente da implementação do gráfico.
"""
@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador