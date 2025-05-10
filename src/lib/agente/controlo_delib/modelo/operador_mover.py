"""
O operador de mover é responsável por mover o agente numa direção específica
no ambiente. Ele utiliza o modelo do mundo para determinar a nova posição do agente
e verificar se a ação é válida.
Define a transforamação (transição de estado) e o custo da ação.
"""
class OperadorMover:

    @property
    def ang(self):
        return self.__ang
    
    @property
    def acao(self):
        return self.__acao
    
    def __init__(self, modelo_mundo, direcao):
        self.__modelo_mundo = modelo_mundo
        self.__direcao = direcao

    def aplicar(self, estado):
        pass

    def custo(self, estado, estado_suc):
        pass