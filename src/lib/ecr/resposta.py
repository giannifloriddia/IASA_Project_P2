class Resposta:

    #Construtor
    def __init__(self, acao):
        self._acao = acao
    
    #Método ainda nao implementado
    def ativar(self, percecao, intensidade = 0):
        raise NotImplementedError("Subclass must implement abstract method, Retorna acao")
