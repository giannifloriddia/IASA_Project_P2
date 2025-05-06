"""
Um nó é uma representação de um estado do problema.
Tem estado, operador, antecessor e custo.
"""
class No:

    """
    Atributos estáticos para contar o número de nós criados e eliminados
    são acedidos com o nome da classe, e não da instância. Um atributo
    estático é o mesmo para todas as instâncias da classe.
    Isso significa que, se um nó for criado ou eliminado, o número de nós
    criados ou eliminados será atualizado para todas as instâncias da classe.
    """
    nos_criados = 0
    nos_eliminados = 0
    nos_max_em_memoria = 0
    
    """
    Propriedades para os atributos profundidade, custo, estado, operador,
    fazendo assim com que somente sejam lidos, e não escritos (read-only).
    """
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
    O nó com menor prioridade é o que será explorado primeiro. A "property"
    faz o efeito de read.
    """
    @property
    def prioridade(self):
        return self.__prioridade
    
    """
    Adicionamos o setter, para que o valor da prioridade possa ser
    alterada. Fazendo assim com que tenha um efeito de write.
    """
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
    Para além disso, se não houver antecessor, o número de nós criados e eliminados
    é inicializado a 0.
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
            No.nos_max_em_memoria = 0
        else:
            self.__profundidade = antecessor.profundidade + 1
        No.nos_criados += 1 #Quando um nó é criado, o número de nós criados é incrementado
        # Calcula o número atual de nós em memória (criados menos eliminados)
        n_nos_em_mem = No.nos_criados - No.nos_eliminados
        # Atualiza o contador de máximo de nós em memória se o número atual for maior
        if n_nos_em_mem > No.nos_max_em_memoria:
            No.nos_max_em_memoria = n_nos_em_mem            
        self.__prioridade = None

    """
    O método __del__ é chamado quando o objeto é destruído,
    ou seja, quando não há mais referências a ele.
    Alteramos o método para que, quando o nó for eliminado,
    o número de nós eliminados seja incrementado.
    """
    def __del__(self):
        No.nos_eliminados += 1