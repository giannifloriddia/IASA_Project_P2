from mod.estado import Estado
#CLASSE É PARA FICAR AQUI MESMO, MAS O NOME É PARA SER ALTERADO

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

    def id_valor(self):
        return hash(self.__posicao)