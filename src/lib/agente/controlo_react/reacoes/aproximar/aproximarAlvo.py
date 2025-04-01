from ecr.prioridade import Prioridade
from .aproximarDir import AproximarDir
from sae.ambiente.direccao import Direccao

"""
Chama AproximarDir para cada direção, usando o construtor da superclasse.
"""
class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([AproximarDir(direcao) for direcao in Direccao])