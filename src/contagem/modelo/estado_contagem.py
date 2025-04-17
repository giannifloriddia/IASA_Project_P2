from mod.estado import Estado

"""
Neste problema, o estado é o valor atual da contagem.
O estado é representado por um número inteiro.
"""
class EstadoContagem(Estado):
    
    def __init__(self, valor):
        self.valor = valor

    """
    O ID do estado é o valor atual da contagem.
    """
    def id_valor(self):
        return self.valor