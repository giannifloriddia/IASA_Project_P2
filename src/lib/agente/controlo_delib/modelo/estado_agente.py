from mod.estado import Estado
"""
EstadoAgente representa o estado de um agente no ambiente.
"""
class EstadoAgente(Estado):

    @property
    def posicao(self):
        return self.__posicao

    #Inicializa a posição
    def __init__(self, posicao):
        self.__posicao = posicao

    """
    O id é o hash da posição do agente.
    """
    def id_valor(self):
        return hash(self.__posicao)