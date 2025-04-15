from ..mec_proc.fronteira import Fronteira

class FronteiraFIFO(Fronteira):

    """
    Fronteira FIFO (First In First Out) - Implementa uma fila.
    Os nós são removidos na ordem em que foram inseridos.
    Ou seja, o primeiro nó adicionado é o primeiro a ser removido.
    """
    def inserir(self, no):
        self._nos.append(no)
