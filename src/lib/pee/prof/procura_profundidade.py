from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_lifo import FronteiraLIFO

"""
No mecanismo de procura em profundidade os nós são
removidos da fronteira na ordem inversa em que foram inseridos.

Na procura em profundidade, a exploração dos nós é feita seguindo sempre um 
caminho até ao seu final antes de retroceder e explorar outros ramos. Ou seja, 
dá-se prioridade aos nós mais recentemente gerados, descendo o mais fundo 
possível na árvore de procura antes de voltar atrás. Esta abordagem é mais 
eficiente em termos de memória, já que apenas é necessário guardar o caminho 
atual desde a raiz até ao nó em análise. No entanto, uma das principais desvantagens 
é que o algoritmo pode ficar preso em ramos muito profundos ou até infinitos, 
especialmente se não houver uma condição clara de paragem.

Além disso, ao contrário da procura em largura, a procura em profundidade 
não garante que a solução encontrada seja a de menor profundidade. 
A sua complexidade temporal é linear e muito menos elevada em comparação 
com a procura em largura, sendo O(b*d),
onde *b* é o fator de ramificação e d é a é a profundidade da procura.
"""
class ProcuraProfundidade(MecanismoProcura):
    
    def __init__(self):
        super().__init__(FronteiraLIFO())