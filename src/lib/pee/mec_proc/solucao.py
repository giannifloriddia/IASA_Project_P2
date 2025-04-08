"""
Uma solução é uma coleção de passos que levam a um nó final.
"""
class Solucao:

    @property
    def dimensao(self):
        return self.__dimensao

    @property
    def custo(self):
        return self.__custo

    def __init__(self, no_final):
        self.__no_final = no_final
        self.__dimensao = 0
        self.__custo = 0.0
        self.__passos = []
        #assert len(self.__passos) >= 1, "A solucao deve ter pelo menos um passo."