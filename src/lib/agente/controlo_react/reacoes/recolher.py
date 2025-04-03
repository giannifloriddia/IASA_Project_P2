#prioridade inversamente proporcional à distância
# 4 instancias de aproximar alvo, cada uma tem estimulo alvo e dispara respotamover nessa direção
from ecr.hierarquia import Hierarquia
from .aproximar.aproximarAlvo import AproximarAlvo
from .explorar.explorar import Explorar
from .explorar.explorarComMemoria import ExplorarComMemoria
from .evitar.evitarObst import EvitarObst

"""
O comportamento Recolher modela o objetivo de recolher alvos, 
combinando 4 sub-comportamentos: AproximarAlvo, EvitarObst, Explorar e ExplorarComMemoria.
A ordem reflete a importância de evitar obstáculos e alcançar o objetivo principal.

Os comportamentos são organizados por prioridade:
1. **EvitarObst**: Primeiro, o agente evita obstáculos para não colidir.
2. **AproximarAlvo**: Depois, aproxima-se do alvo.
3. **Explorar**: Por último, se não estiver a realizar nenhum dos outros comportamentos, explora. 
"""
class Recolher(Hierarquia):
    def __init__(self):
        super().__init__([EvitarObst(), AproximarAlvo(), ExplorarComMemoria(), Explorar()])