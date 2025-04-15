from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_fifo import FronteiraFIFO

class ProcuraLargura(MecanismoProcura):

    """
    Mecanismo de procura em largura.
    A fronteira é uma lista de nós que serão expandidos.
    Os nós são removidos da fronteira na ordem em que foram inseridos.
    """
    def __init__(self):
        super().__init__(FronteiraFIFO())