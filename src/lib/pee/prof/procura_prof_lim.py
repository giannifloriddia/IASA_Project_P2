from .procura_profundidade import ProcuraProfundidade

"""
Queremos ter um mecanismo que tenha os benefícios da procura em largura,
tal como a solução ótima e completa, mas que consuma memória similar à
procura em profundidade.
Para isso, limitamos a profundidade máxima da procura.
A procura em profundidade limitada é uma técnica que combina
a profundidade e a largura, permitindo explorar os nós até uma profundidade
máxima definida.

A limitação da profundidade da procura leva à exploração de nós em largura,
mantendo a complexidade de memória linear
O problema é que, a profundidade a que se encontra a solução pode não ser conhecida
"""
class ProcuraProfLim(ProcuraProfundidade):

    def __init__(self, prof_max = 10):
        super().__init__()
        self._prof_max = prof_max

    """
    Este mecanismo expande os nós até à profundidade máxima definida.
    Ou seja, expande se a profundidade do nó for menor que a profundidade máxima.
    """
    def _expandir(self, problema, no):
        return super()._expandir(problema, no) if no.profundidade < self._prof_max else []
    
    """
    Alterei o método de representação da classe para facilidadede nos prints
    """
    def __repr__(self):
        return "Procura em Profundidade Limitada"