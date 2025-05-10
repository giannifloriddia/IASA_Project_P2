from pee.melhor_prim.fronteira_prioridade import FronteiraPrioridade
from .fronteira_prioridade import FronteiraPrioridade
from ..mec_proc.procura_grafo import ProcuraGrafo
from abc import ABC


"""
Na procura melhor primeiro, a procura é feita com base num critério 
de avaliação diferente da profundidade, como por exemplo a distância,
o tempo ou o custo.
Utiliza uma função f para avaliação de cada nó n gerado, quanto menor o valor de f(n),
melhor é o nó. Os nós que ainda não foram explorados (abertos + fechados) 
são organizados de forma crescente com base no valor de f(n), ou seja, os nós com menor 
valor são analisados primeiro.
Como precisa de uma memória de nós explorados, extende a classe ProcuraGrafo.

As variantes principais da procura melhor-primeiro são:
- Procura de Custo Uniforme f(n) = g(n)
- Procura Sôfrega f(n) = h(n)
- Procura A* f(n) = g(n) + h(n)

"""
class ProcuraMelhorPrim(ProcuraGrafo, ABC):

    """
    Tem uma fronteira de prioridade, é inicializado o avaliador,
    e é chamado o superconstrutor da classe ProcuraGrafo com a fronteira de prioridade.
    """
    def __init__(self, avaliador):
        fronteira = FronteiraPrioridade(avaliador)
        self._avaliador = avaliador
        self.contador = 0
        super().__init__(fronteira)

    """
    O método verifica se o nó já foi explorado ou se o custo do nó atual 
    é menor que o custo do nó já explorado.
    Se o nó não foi explorado ou se o custo do nó atual é menor, 
    ele deve ser mantido na fronteira.
    """
    def _manter(self, no):
        verificar = no.estado not in self._explorados or no.custo < self._explorados[no.estado].custo
        #Adicionado pela indicação do professor
        if not verificar:
            #Conta o número de nós/estados repetidos
            self.contador += 1
        return verificar
