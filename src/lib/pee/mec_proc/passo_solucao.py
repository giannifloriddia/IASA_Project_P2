from dataclasses import dataclass
from mod.estado import Estado
from mod.operador import Operador

#fica read/write porque anotação gera getter e setter
@dataclass
class PassoSolucao:
    estado: Estado
    operador: Operador