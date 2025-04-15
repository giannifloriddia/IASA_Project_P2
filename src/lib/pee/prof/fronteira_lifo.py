from ..mec_proc.fronteira import Fronteira

class FronteiraLIFO(Fronteira):

    """ 
    LIFO (Last In First Out) - Implementa uma pilha.
    Os nós são removidos na ordem inversa em que foram inseridos.
    Ou seja, o último nó adicionado é o primeiro a ser removido.
    """
    def inserir(self, no):
        self._nos.insert(0, no)
        # Adiciona o nó no início da lista, para que o último nó adicionado seja o primeiro a ser removido