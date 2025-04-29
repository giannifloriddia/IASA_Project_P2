from abc import ABC, abstractmethod
from .no import No
from .solucao import Solucao

"""
Um mecanismo de procura é um algoritmo que busca uma solução para um problema.
Um mecanismo de procura tem uma fronteira, que é uma coleção de nós que estão prontos para serem expandidos.
Tem de ter métodos para iniciar a memória, memorizar nós e expandir nós.
"""
class MecanismoProcura(ABC):

    @property
    def nos_processados(self):
        return No.nos_criados

    @property
    def nos_em_memoria(self):
        return No.nos_criados - No.nos_eliminados

    def __init__(self, fronteira):
        self._fronteira = fronteira

    #Inicia a memória, ou seja, inicializa uma fronteira vazia.
    def _iniciar_memoria(self):
        self._fronteira.iniciar()

    #Memoriza um nó é adicioná-lo à fronteira.
    def _memorizar(self, no):
        self._fronteira.inserir(no)
    
    """
    O método procurar é o método principal do mecanismo de procura.
    Ele recebe um problema e procura uma solução para esse problema.
    Inicia a mémoria e cria um nó inicial a partir do estado inicial do problema,
    e memoriza-o (adiciona-o à fronteira).
    Enquanto a fronteira não estiver vazia, remove o nó inicial da fronteira
    e guarda-o numa variável auxiliar.
    Procura um nó na fronteira que é o estado objetivo.
    Se o nó for o estado objetivo, retorna a solução.
    Se não for, expande o nó e adiciona os nós sucessores à fronteira (memoriza-os).
    Se a fronteira estiver vazia, retorna None por defeito.
    """
    def procurar(self, problema):
        
        self._iniciar_memoria()
        no = No(problema.estado_inicial)
        self._memorizar(no)
        
        while not self._fronteira.vazia:

            no = self._fronteira.remover()

            if problema.objetivo(no.estado):
                return Solucao(no)
            
            for no_sucessor in self._expandir(problema, no):
                self._memorizar(no_sucessor)
        
    """
    O método expandir recebe um problema e um nó.
    Ele expande o nó e retorna uma lista de nós sucessores.
    O nó sucessor é criado a partir do estado sucessor e do nó pai.
    O custo do nó sucessor (cumulativo) é o custo do nó pai mais o custo do operador.
    O nó sucessor é adicionado à lista de nós sucessores.
    """
    def _expandir(self, problema, no):
        sucessores = []
        estado = no.estado
        
        for operador in problema.operadores:
            estado_suc = operador.aplicar(estado)
            
            if estado_suc is not None:
                custo = no.custo + operador.custo(estado, estado_suc)
                no_sucessor = No(estado_suc, operador, no, custo)
                sucessores.append(no_sucessor)
                
        return sucessores