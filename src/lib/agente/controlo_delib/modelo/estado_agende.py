from mod.estado import Estado
#CLASSE É PARA FICAR AQUI MESMO, MAS O NOME É PARA SER ALTERADO

"""
EstadoAgente representa o estado de um agente no ambiente.
"""
class EstadoAgende(Estado):

    @property
    def posicao(self):
        return self.__posicao

    def __init__(self, posicao):
        self.__posicao = posicao

    #Assim?
    def id_valor(self):
        return self._posicao.__hash__()