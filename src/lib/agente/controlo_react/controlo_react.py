"""
Implementa o processamento interno
do agente que relaciona a percecao com a acao.
Implementa a "inteligencia do agente"
"""
class ControloReact:

    #Construtor da classe
    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    """
    Ativa o comportamento de acordo com a perceção
    recebida e retorna uma ação.
    """
    def processar(self, percecao):
        return self.__comportamento.ativar(percecao)