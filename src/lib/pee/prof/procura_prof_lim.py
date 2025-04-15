from .procura_profundidade import ProcuraProfundidade

class ProcuraProfLim(ProcuraProfundidade):

    def __init__(self, prof_max = 10):
        super().__init__()  # Call parent constructor to initialize _fronteira
        self._prof_max = prof_max

    def _expandir(self, problema, no):
        return super()._expandir(problema, no) if no.profundidade < self._prof_max else []