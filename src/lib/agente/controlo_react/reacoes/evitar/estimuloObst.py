"""
Esta classe representa um estímulo de contacto com um obstáculo.
O estímulo é definido pela direção e intensidade do contacto.
A intensidade é um valor que representa a força do contacto, onde 1 é o valor padrão.
Se não houver contacto, a retorna 0, senão retorna a própria intensidade.
"""
class EstimuloObst:
    def __init__(self, direcao, intensidade=1):
        self._direcao = direcao
        self.__intensidade = intensidade
    
    def detetar(self, percecao):
        if percecao.contacto_obst(self._direcao):
            return self.__intensidade
        else:
            return 0