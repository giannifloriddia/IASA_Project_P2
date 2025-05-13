import math
from agente.controlo_delib.modelo.estado_agente import EstadoAgente
from mod.operador import Operador
from sae.agente.accao import Accao

"""
O operador de mover é responsável por mover o agente numa direção específica
no ambiente. Ele utiliza o modelo do mundo para determinar a nova posição do agente
e verificar se a ação é válida.
Define a transforamação (transição de estado) e o custo da ação.
"""
class OperadorMover(Operador):

    @property
    def ang(self):
        return self.__ang
    
    @property
    def acao(self):
        return self.__acao
    
    def __init__(self, modelo_mundo, direcao):
        self.__modelo_mundo = modelo_mundo
        self.__ang = direcao.value
        self.__acao = Accao(direcao) #ou direccao = direcao

    def aplicar(self, estado):
        nova_posicao = self.__translacao(estado.posicao, self.__acao.passo, self.__ang)
        novo_estado = EstadoAgente(nova_posicao)
        if novo_estado in self.__modelo_mundo:
            return novo_estado

    """
    O custo mínimo é o valor máximo entre 1 e a 
    distância entre o estado atual e o estado sucessor.
    """
    def custo(self, estado, estado_suc):
        return max(1, math.dist(estado.posicao, estado_suc.posicao))

    def __translacao(self, posicao, distancia_desl, ang_desl):
        #desestruturação de objetos
        x, y = posicao
        dx = round(distancia_desl * math.cos(ang_desl))
        dy = -round(distancia_desl * math.sin(ang_desl))
        nova_posicao = x + dx, y + dy
        return nova_posicao