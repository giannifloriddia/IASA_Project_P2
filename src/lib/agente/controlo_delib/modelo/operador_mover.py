class OperadorMover:

    @property
    def ang(self):
        return self.__ang
    
    @property
    def acao(self):
        return self.__acao
    
    def __inti__(self, modelo_mundo, direcao):
        self.__modelo_mundo = modelo_mundo
        self.__direcao = direcao

    def aplicar(self, estado):
        pass

    def custo(self, estado, estado_suc):
        pass