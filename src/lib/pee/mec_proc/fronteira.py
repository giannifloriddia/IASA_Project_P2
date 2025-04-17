from abc import ABC, abstractmethod

"""
Uma fronteira é uma coleção de nós que estão prontos para serem expandidos.
Tem de ter métodos para inserir e remover nós.
Uma fronteira pode estar vazia ou não, se estiver vazia,
é porque estamos no primeiro elemento da árvore, ou porque chegámos ao final da mesma.
"""
class Fronteira(ABC):

    """
    É complilado em tempo de execução, retornando
    True se a fronteira estiver vazia e False caso contrário.
    """
    @property
    def vazia(self):
        return len(self._nos) == 0

    #Chama o método iniciar quando a classe é instanciada.
    def __init__(self):
        self.iniciar()

    #Inicializa a fronteira com um array vazio.
    def iniciar(self):
        self._nos = []

    @abstractmethod
    def inserir(self, no):
        """ Insere um nó na fronteira. """

    #Remove o nó do início da lista e retorna-o.
    def remover(self):
        return self._nos.pop(0)