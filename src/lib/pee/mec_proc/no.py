"""
Um nó é uma representação de um estado do problema.
Tem estado, operador, antecessor e custo.
"""
class No:

    #atributos estáticos para contar o número de nós criados e eliminados
    #são acedidos com o nome da classe, e não da instância
    nos_criados = 0
    nos_eliminados = 0
    
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
    Adicionamos a propriedade prioridade para que o nó possa ser comparado
    com outros nós, de acordo com a prioridade.
    A prioridade é um valor que representa a importância do nó na busca.
    O nó com menor prioridade é o que será explorado primeiro.
    """
    #Read
    @property
    def prioridade(self):
        return self.__prioridade
    
    #Write
    @prioridade.setter
    def prioridade(self, valor):
        self.__prioridade = valor

    #Comparação para saber qual é menor
    def __lt__(self, outro_no):
        return self.__prioridade < outro_no.__prioridade
    
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
        if antecessor is None:
            self.__profundidade = 0
            No.nos_criados = 0
            No.nos_eliminados = 0
        else:
            self.__profundidade = antecessor.profundidade + 1
        #self.__profundidade = 0  if antecessor is None else antecessor.profundidade + 1
        No.nos_criados += 1
        self.__prioridade = None

    def __del__(self):
        No.nos_eliminados += 1