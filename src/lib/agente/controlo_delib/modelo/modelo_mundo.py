from agente.controlo_delib.modelo.estado_agende import EstadoAgende
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento
import math

"""
A classe ModeloMundo representa o modelo do mundo do agente.
"""
class ModeloMundo:
    
    @property
    def alterado(self):
        return self.__alterado
    
    @property
    def elementos(self):
        return self.__elementos
    
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao] #passar o proprio valor ModeloMundo (self)
        self.__alterado = False

    #metodo para facilitar a escrita (if estado in (instancia do mundo))
    #implemenação do operador in
    def __contains__(self, estado):
        return estado in self._estados
    
    def obter_estado(self):
        return self.__estado

    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao) #retorna none para não dar exceção se não existir o estado (default value)

    def distacia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)

    def atualizar(self, percecao):
        self.__estado = EstadoAgende(percecao.posicao)
        self.__alterado = self.__elementos != percecao.elementos
        if self.__alterado:
            self.__elementos = percecao.elementos
            self.__estados = [EstadoAgende(posicao) for posicao in percecao.posicoes]

    def mostrar(self, vista):
        #tuplos de estados e elementos
        #primeiro elemento chave, segundo valor
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)