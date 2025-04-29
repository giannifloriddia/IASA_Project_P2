from ..mec_proc.fronteira import Fronteira
import heapq


"""
A classe FronteiraPrioridade é uma implementação de uma fronteira que utiliza
uma fila de prioridade para armazenar os nós a serem explorados.
A fila de prioridade é implementada com a biblioteca heapq, que fornece uma
estrutura de dados eficiente para gerenciar a fila de prioridade.

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
    
    def inserir(self, no):
        no.prioridade = self.__avaliador.prioridade(no)
        heapq.heappush(self._nos, no)
    
    def remover(self):
        return heapq.heappop(self._nos)
