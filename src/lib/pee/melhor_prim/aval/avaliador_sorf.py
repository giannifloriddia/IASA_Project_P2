from .avaliador_heur import AvaliadorHeur

"""
Na procura sôfrega, o avaliador, ou seja,
a função f(n) é definida como somente a heurística.
"""
class AvaliadorSorf(AvaliadorHeur):

    """
    Prioridade definida por f(n) = h(n).
    (sendo h(n) a heurística do nó n)
    """
    def prioridade(self, no):
        return self.heuristica.h(no.estado)