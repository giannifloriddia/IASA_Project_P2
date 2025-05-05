from pee.melhor_prim.procura_melh_prim import ProcuraMelhorPrim

"""
Os métodos de procura não informada exploram o espaço de estados 
sem usar qualquer conhecimento específico sobre o problema. São 
estratégias genéricas e fazem uma exploração exaustiva, testando 
muitos caminhos possíveis de forma cega (como a procura em largura ou 
profundidade).

Por outro lado, os métodos de procura informada usam informação 
sobre o domínio do problema (como estimativas de distância ao objetivo) 
para guiar a procura. Isso permite uma exploração mais seletiva e 
eficiente, focando nos caminhos mais promissores.
"""
class ProcuraInformada(ProcuraMelhorPrim):
    
    """
    A procura informada necessita de uma heurística, que é uma função que estima 
    o custo de chegar ao objetivo a partir de um determinado estado. Essa heurística 
    é usada para avaliar os nós e determinar a ordem em que eles são explorados.
    O método, inicializa a heurística e retorna o procurar da super classe com
    o problema como parâmetro.
    """
    def procurar(self, problema, heuristica):
        self._avaliador.heuristica = heuristica
        return super().procurar(problema)