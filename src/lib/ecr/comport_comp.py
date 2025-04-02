"""
Utilizamos caminhos absolutos para importar do python path
e relativos para importar dentro do projeto
"""
from abc import ABC, abstractmethod
from .comportamento import Comportamento

class ComportComp(Comportamento, ABC):

    def __init__(self, comportamentos):
        self.__comportamentos = comportamentos

    """
    Vai a cada comportamento da lista de comportamentos e ativa cada um,
    guardando as acoes resultantes numa outra lista de acoes se elas existirem
    (neste caso não precisámos de utilizar o is not None pois não estamos a comparar inteiros).
    Depois chama o metodo selecionar_acao se acoes > 0,
    usando como parametro a lista de acoes, para escolher a acao a ser tomada.
    """
    def ativar(self, percecao):
        acoes = []
        for comportamento in self.__comportamentos:
            acao = comportamento.ativar(percecao)
            if acao:
                acoes.append(acao)
        if acoes:
            return self.selecionar_acao(acoes)
        
    """
    Um comportamento composto é composto por várias ações, e os
    métodos de selecionar essa ação são implementados diferentemente
    pelas classes que herdam de ComportComp.
    """
    @abstractmethod
    def selecionar_acao(self, acoes):
        """Seleciona uma acao a partir de uma lista de acoes."""