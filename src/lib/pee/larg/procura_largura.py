from ..mec_proc.mecanismo_procura import MecanismoProcura
from .fronteira_fifo import FronteiraFIFO


"""
Na procura em largura, os nós são explorados pela ordem em que 
são gerados, começando pelos mais antigos.

Isso significa que todos os nós de um determinado nível são examinados 
antes de passar para o nível seguinte. Essa abordagem garante uma exploração 
sistemática e completa de todas as possibilidades até encontrar a solução, isso
garante que a solução encontrada seja a de menor profundidade possível.

No entanto, uma das principais desvantagens deste método é o elevado consumo de memória, 
uma vez que é necessário armazenar todos os nós gerados em cada nível, 
o que pode tornar o algoritmo inviável para problemas com grandes espaços de estados.

Além disso, a sua complexidade temporal é exponencial — O(b^d), onde b é o fator de 
ramificação e d é a profundidade da procura — o que significa que o tempo necessário 
para encontrar a solução pode crescer rapidamente à medida que o problema se torna mais complexo.
"""
class ProcuraLargura(MecanismoProcura):

    def __init__(self):
        super().__init__(FronteiraFIFO())

    """
    Alterei o método de representação da classe para facilidadede nos prints
    """
    def __repr__(self):
        return "Procura em Largura"