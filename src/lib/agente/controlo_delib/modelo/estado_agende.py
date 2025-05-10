from mod.estado import Estado
#CLASSE É PARA FICAR AQUI MESMO, MAS O NOME É PARA SER ALTERADO

"""
EstadoAgente representa o estado de um agente no ambiente.
"""
class EstadoAgende(Estado):

    @property
    def posicao(self):
        return self.__posicao

    #Inicializa a posição
    def __init__(self, posicao):
        self.__posicao = posicao

    """
    Dá um id ao valor com o método que redefinimos
    na classe de Estado.
    """
    def id_valor(self):
        return self.__hash__()