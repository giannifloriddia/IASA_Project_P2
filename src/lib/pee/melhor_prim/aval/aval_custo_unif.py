from .avaliador import Avaliador

"""
Na procura de custo uniforme, o avaliador, ou seja,
a função f(n) é definida como o custo do nó n.
Sendo o custo recursivo, o custo do nó n é a soma
do custo desde o estado inicial até ao nó n.
"""
class AvaliadorCustoUnif(Avaliador):

    """
    Prioridade definida por f(n) = g(n).
    (sendo g(n) o custo do nó n)
    """
    def prioridade(self, no):
        return no.custo