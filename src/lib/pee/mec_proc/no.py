"""
Um nó é uma representação de um estado do problema.
Tem estado, operador, antecessor e custo.
"""
class No:
    
    #Propriedades, para acesso aos atributos privados (read only)
    @property
    def profundidade(self):
        return self.__profundidade
    
    @property
    def custo(self):
        return self.__custo
    
    @property
    def estado(self):
        return self.__estado
    
    @property
    def operador(self):
        return self.__operador
    
    @property
    def antecessor(self):
        return self.__antecessor

    """
    Inicia um nó com o estado (obrigatório), operador, 
    antecessor e custo, com parâmetros defaulf None e 0 para o custo.
    A profundidade é 0 se o nó não tiver antecessor,
    caso contrário, é calculado a partir do nó antecessor +1.
    """
    def __init__(self, estado, operador=None, antecessor=None, custo=0.0):
        self.__estado = estado
        self.__operador = operador
        self.__antecessor = antecessor
        self.__custo = custo
        self.__profundidade = 0 if antecessor is None else antecessor.profundidade + 1