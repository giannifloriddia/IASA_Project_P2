from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

class ProcuraProfundidade(MecanismoProcura):
    
    """
    Mecanismo de procura em profundidade.
    A fronteira é uma lista de nós que serão expandidos.
    Os nós são removidos da fronteira na ordem inversa em que foram inseridos.
    """
    def __init__(self):
        super().__init__(FronteiraLIFO())