from .aval.avaliador_aa import AvaliadorAA
from .procura_informada import ProcuraInformada

class ProcuraAA(ProcuraInformada):
    
    def __init__(self):
        super().__init__(AvaliadorAA())