from .comport_comp import ComportComp

"""
Os comportamentos estão organizados numa hierarquia fixa de
subsunção (supressão e substituição).

Retorna a açao em primeiro lugar na hierarquia,
os primeiros da lista são os mais prioritarios
ou seja retornar a que estiver no index 0.
"""
class Hierarquia(ComportComp):
    def selecionar_acao(self, acoes):
        return acoes[0]