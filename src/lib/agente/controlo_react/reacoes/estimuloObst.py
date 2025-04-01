

class EstimuloObst:
    def __init__(self, direcao, intensidade=1):
        self._direcao = direcao
        self.__intensidade = intensidade
    
    def detetar(self, percecao):
        if percecao.contacto_obst(self._direcao):
            return self.__intensidade
        else:
            return 0