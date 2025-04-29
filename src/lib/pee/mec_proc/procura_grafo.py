from abc import ABC, abstractmethod
from .mecanismo_procura import MecanismoProcura

class ProcuraGrafo(MecanismoProcura, ABC):

    """
    O método iniciar_memoria inicializa 
    a memória da procura com a superclasse,
    e após inicializa a memória de explorados
    como um dicionário vazio.
    """
    def _iniciar_memoria(self):
        super()._iniciar_memoria()
        self._explorados = {}

    """
    Memoriza o nó, se o nó não estiver na memória de explorados.
    Se o nó já estiver na memória de explorados,
    não o memoriza.
    Após a verificação, o nó é adicionado à memória de explorados.
    """
    def _memorizar(self, no):
        if self._manter(no):
            super()._memorizar(no)
        self._explorados[no.estado] = no
    @abstractmethod
    def _manter(self, no):
        """retorna booleano"""