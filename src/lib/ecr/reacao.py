from .comportamento import Comportamento

class Reacao(Comportamento):

    #Construtor da classe Reacao
    def __init__(self, estimulo, resposta):
        self.__estimulo = estimulo
        self.__resposta = resposta

    """
    Modelo aplicado de acordo com o diagrama de 
    sequências do slide 4 do P2. Vai deter a 
    intensidade do estímulo e se for maior que 0, 
    vai ativar a resposta e retornar a ação.
    """
    def ativar(self, percecao):
        intensidade = self.__estimulo.detetar(percecao)
        if intensidade > 0:
            return self.__resposta.ativar(percecao, intensidade)