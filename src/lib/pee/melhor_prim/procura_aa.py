from .aval.avaliador_aa import AvaliadorAA
from .procura_informada import ProcuraInformada

"""
Na Procura A*, a função de avaliação é f(n) = g(n) + h(n), 
onde g(n) é o custo real até ao nó e h(n) é a estimativa do 
custo até ao objetivo. Este método procura minimizar o custo total da 
solução, combinando o que já foi percorrido com o que falta percorrer.

Para garantir que encontra a melhor solução, A* usa uma heurística 
admissível, ou seja, uma função h(n) que nunca sobrestima o custo 
real restante. Esta propriedade torna a heurística optimista, pois assume 
sempre que o objetivo está mais próximo ou igualmente distante do que 
realmente está.

"""
class ProcuraAA(ProcuraInformada):
    
    """
    Inicializa a procura informada com o AvaliadorAA,
    que é o avaliador de procura A*.
    """
    def __init__(self):
        super().__init__(AvaliadorAA())

    """
    Adicionado por conveniência nos prints.
    """
    def __repr__(self):
        return "Procura A*"