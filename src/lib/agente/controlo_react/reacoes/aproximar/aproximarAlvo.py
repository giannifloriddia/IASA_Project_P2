from ecr.prioridade import Prioridade
from .aproximarDir import AproximarDir
from sae.ambiente.direccao import Direccao

"""
Chama AproximarDir para cada direção (Norte, Sul, Este e Oeste), 
usando o construtor da superclasse passando a lista de direções.
"""
class AproximarAlvo(Prioridade):
    def __init__(self):
        super().__init__([AproximarDir(direcao) for direcao in Direccao])