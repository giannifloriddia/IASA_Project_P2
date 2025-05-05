from ..mec_proc.fronteira import Fronteira
import heapq

"""
A classe FronteiraPrioridade é uma implementação de uma fronteira que utiliza
uma fila de prioridade para armazenar os nós a serem explorados.
A fila de prioridade é implementada com a biblioteca heapq, que possibilita o 
acesso a listas com relação de ordem entre os elementos
"""
class FronteiraPrioridade(Fronteira):

    """
    Inicia o superconstrutor da classe Fronteira,
    e inicializa o atributo __avaliador com o 
    avaliador passado como parâmetro.
    O avaliador é responsável por determinar a prioridade 
    dos nós na fila de prioridade.
    """
    def __init__(self, avaliador):
        super().__init__()
        self.__avaliador = avaliador
    
    """
    Um nó é inserido na fila de prioridade com base na sua prioridade.
    A prioridade é determinada pelo avaliador, que é passado como parâmetro
    no construtor da classe.
    O nó é adicionado à lista de nós através da função heappush, que
    insere o nó na lista de forma que a ordem de prioridade seja mantida.
    """
    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        heapq.heappush(self._nos, no)
    
    """
    Para remover um nó, utilizamos a função heappop da biblioteca heapq,
    que remove e retorna o nó com a menor prioridade da lista de nós.
    """
    def remover(self):
        return heapq.heappop(self._nos)
