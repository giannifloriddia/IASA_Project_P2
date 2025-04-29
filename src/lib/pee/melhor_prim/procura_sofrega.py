from .aval.avaliador import Avaliador
from .procura_informada import ProcuraInformada

class ProcuraSofrega(ProcuraInformada):
    
    def __init__(self):
        super().__init__(Avaliador())