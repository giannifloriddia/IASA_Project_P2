from abc import ABC, abstractmethod

"""
A função heurística h(n) é usada nos métodos de procura 
informada para estimar o custo restante desde um nó n até 
ao objetivo. Embora possa não ser exata, ajuda a orientar a procura 
de forma mais eficiente, evitando caminhos menos promissores.

Esta função baseia-se apenas no estado atual e no estado objetivo, 
ignorando o caminho que levou até n. Assim, a heurística traduz 
conhecimento do problema que permite priorizar os nós que parecem mais 
próximos da solução, melhorando o desempenho da procura em termos de tempo 
e espaço.
"""
class Heuristica(ABC):
    
    @abstractmethod
    def h(self, estado):
        """retorna double."""