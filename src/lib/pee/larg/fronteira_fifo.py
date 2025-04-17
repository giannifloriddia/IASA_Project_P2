from ..mec_proc.fronteira import Fronteira

"""
Fronteira FIFO (First In First Out) - Implementa uma fila.
Os nós são removidos na ordem em que foram inseridos.
Ou seja, o primeiro nó adicionado é o primeiro a ser removido.
"""
class FronteiraFIFO(Fronteira):

    #Nó é adicionado ao final da lista
    def inserir(self, no):
        self._nos.append(no)
