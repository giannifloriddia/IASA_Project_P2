from abc import ABC, abstractmethod
from .mecanismo_procura import MecanismoProcura

"""
Um mecanismo de procura em grafo é um algoritmo 
que busca uma solução para um problema,
mas que tem uma memória de explorados, ou seja, 
uma memória que guarda os nós que já foram explorados.
"""
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
    Se o nó já estiver na memória de explorados, não o memoriza.
    Após a verificação, o nó é adicionado à memória de explorados.
    """
    def _memorizar(self, no):
        if self._manter(no):
            super()._memorizar(no)
            self._explorados[no.estado] = no
    
    """
    Método abstrato _manter o nó na memória de explorados,
    ou seja, verifica se o nó deve ser mantido na memória.
    """
    @abstractmethod
    def _manter(self, no):
        """retorna booleano"""