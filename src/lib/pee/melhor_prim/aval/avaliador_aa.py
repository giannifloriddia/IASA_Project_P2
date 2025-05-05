from .avaliador_heur import AvaliadorHeur

"""
Na procura A*, o avaliador, ou seja,
a função f(n) é definida como a soma da heurística com o custo.
"""
class AvaliadorAA(AvaliadorHeur):

    """
    Prioridade definida por f(n) = g(n) + h(n).
    (sendo h(n) a heurística do nó n e g(n) o custo do nó n)
    """
    def prioridade(self, no):
        return no.custo + self.heuristica.h(no.estado)