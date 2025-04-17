from .passo_solucao import PassoSolucao

"""
Uma solução é uma coleção de passos que levam a um nó final.
propriedades privadas são calculadas em tempo de execucao
"""
class Solucao:

    """
    A dimensão de uma solução é
    simplesmente a profundidade do nó final.
    """
    @property
    def dimensao(self):
        return self.__no_final.profundidade

    """
    O custo é o custo do nó final, que
    é o custo cumulativo dos nós antecessores
    """
    @property
    def custo(self):
        return self.__no_final.custo
    
    """
    É passado um nó final como parâmetro 
    e criada uma lista de passos vazia.
    Enquanto o nó antecessor existir,
    criamos um passo de solução a partir 
    do nó antecessor e do operador.
    O passo é inserido na lista de passos.
    E a variável auxiliar nó é atualizada 
    para o nó antecessor antes de repetir o ciclo.
    """
    def __init__(self, no_final):
        self.__no_final = no_final
        self.__passos = []
        no = no_final
        while no.antecessor:
            passo = PassoSolucao(no.antecessor.estado, no.operador)
            self.__passos.insert(0, passo)
            no = no.antecessor
        #assert len(self.__passos) >= 1, "A solucao deve ter pelo menos um passo."
    
    """
    Transformamos numa classe iteravel, para podermos iterar sobre os passos da solução.
    Vão ser devolvidos os passos da solução, que são os passos que levam ao nó final.
    """
    def __iter___ (self):
        return iter(self.__passos)
    
    """
    Torna a classe indexavel, para podermos aceder aos passos da solução
    através do índice.
    """
    def __getitem__(self, index):
        return self.__passos[index]