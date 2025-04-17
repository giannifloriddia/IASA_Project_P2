from ..mec_proc.fronteira import Fronteira

""" 
LIFO (Last In First Out) - Implementa uma pilha.
Os nós são removidos na ordem inversa em que foram inseridos.
Ou seja, o último nó adicionado é o primeiro a ser removido.
"""
class FronteiraLIFO(Fronteira):

    #Nó é adicionado no ínicio da lista
    def inserir(self, no):
        self._nos.insert(0, no)