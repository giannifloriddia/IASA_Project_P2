from .aval.avaliador_sorf import AvaliadorSorf
from .procura_informada import ProcuraInformada

"""
Na Procura Sôfrega (Greedy Search), a função de avaliação 
é f(n) = h(n), ou seja, a decisão sobre qual nó explorar depende 
apenas da estimativa do custo até ao objetivo. Este método 
ignora o custo já percorrido, focando-se apenas em avançar 
rapidamente para o destino. Apesar de ser eficiente em muitos casos, 
pode seguir caminhos enganosos, resultando em soluções sub-óptimas.
"""
class ProcuraSofrega(ProcuraInformada):
    
    """
    Inicializa a procura informada com o AvaliadorSorf,
    que é o avaliador de procura sôfrega.
    """
    def __init__(self):
        super().__init__(AvaliadorSorf())

    """
    Adicionado por conveniência nos prints.
    """
    def __repr__(self):
        return "Procura Sofrega"