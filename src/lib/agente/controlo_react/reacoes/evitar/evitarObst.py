from ecr.hierarquia import Hierarquia
from sae import Direccao
from .evitarDir import EvitarDir

"""
Chama EvitarDir para cada direcao possivel.
Esta reacao tem como objetivo evitar um obstaculo.
"""
class EvitarObst(Hierarquia):
    def __init__(self):
        super().__init__([EvitarDir(direcao) for direcao in Direccao])