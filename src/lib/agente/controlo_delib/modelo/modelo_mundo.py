from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from agente.controlo_delib.modelo.operador_mover import OperadorMover
from plan.modelo.modelo_plan import ModeloPlan
from sae.ambiente.direccao import Direccao
from sae.ambiente.elemento import Elemento
import math

"""
A classe ModeloMundo representa o modelo do mundo do agente.
"""
class ModeloMundo(ModeloPlan):
    
    """
    Propriedade que retorna se o modelo do mundo foi alterado.
    """
    @property
    def alterado(self):
        return self.__alterado
    
    """
    Propriedade que retorna o dicionário de elementos do modelo do mundo.
    """
    @property
    def elementos(self):
        return self.__elementos
    
    def __init__(self):
        self.__estado = None
        self.__estados = []
        self.__elementos = {}
        #passa o proprio valor ModeloMundo (self) e cada diração em Direccao
        self.__operadores = [OperadorMover(self, direcao) for direcao in Direccao]
        self.__alterado = False

    #metodo para facilitar a escrita (if estado in (instancia do mundo))
    #implementação do operador in
    def __contains__(self, estado):
        return estado in self.__estados
    
    #obter estado atual
    def obter_estado(self):
        return self.__estado

    #obter estados do modelo
    def obter_estados(self):
        return self.__estados

    def obter_operadores(self):
        return self.__operadores

    def obter_elemento(self, estado):
        return self.__elementos.get(estado.posicao) #retorna none para não dar exceção se não existir o estado (default value)

    """
    Define a distância entre dois estados.
    """
    def distancia(self, estado):
        return math.dist(estado.posicao, self.__estado.posicao)

    """
    Atualiza o modelo do mundo com a perceção recebida.
    O método atualiza o estado atual do agente e verifica se houve alteração
    nos elementos do ambiente. Se houve alteração, atualiza a lista de elementos
    e atualiza a lista de estados de acordo com a perceção recebida 
    """
    def atualizar(self, percecao):
        self.__estado = EstadoAgente(percecao.posicao)
        self.__alterado = self.__elementos != percecao.elementos
        if self.__alterado:
            self.__elementos = percecao.elementos
            self.__estados = [EstadoAgente(posicao) for posicao in percecao.posicoes]

    """
    Mostra a vista do modelo do mundo utilizando
    funções da classe vista da SAE.
    """
    def mostrar(self, vista):
        #tuplos de estados e elementos
        #primeiro elemento chave, segundo valor
        for posicao, elemento in self.__elementos.items():
            if elemento in [Elemento.ALVO, Elemento.OBSTACULO]:
                vista.mostrar_elemento(posicao, elemento)
        vista.marcar_posicao(self.__estado.posicao)