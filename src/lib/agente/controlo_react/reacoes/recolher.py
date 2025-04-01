#prioridade inversamente proporcional à distância
# 4 instancias de aproximar alvo, cada uma tem estimulo alvo e dispara respotamover nessa direção
from ecr.hierarquia import Hierarquia
from .aproximar.aproximarAlvo import AproximarAlvo
from .explorar.explorar import Explorar
from .explorar.explorarComMemoria import ExplorarComMemoria
from .evitar.evitarObst import EvitarObst

class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([EvitarObst(), AproximarAlvo(), Explorar()])