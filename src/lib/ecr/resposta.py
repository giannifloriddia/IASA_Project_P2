"""
Define uma resposta a estímulos, em termos de 
ação a realizar e da respectiva prioridade
"""
class Resposta:

    #Construtor
    def __init__(self, acao):
        self._acao = acao
    
    """
    Ativa a ação de acordo com a perceção
    recebida e retorna uma ação. Se a perceção
    for diferente de None, a ação é ativada
    """
    def ativar(self, percecao, intensidade = 0):
        if percecao is not None:
            self._acao.prioridade = intensidade
            return self._acao
