from .comport_comp import ComportComp

"""
Retorna a açao em primeiro lugar na hierarquia,
os primeiros da lista são os mais prioritarios
ou seja retornar a que estiver no index 0
"""
class Hierarquia(ComportComp):
    def selecionar_acao(self, acoes):
        return acoes[0]