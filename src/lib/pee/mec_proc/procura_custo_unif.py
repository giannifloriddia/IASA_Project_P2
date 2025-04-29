from .procura_melh_prim import ProcuraMelhorPrim
from ..melhor_prim.aval.aval_custo_unif import AvaliadorCustoUnif

class ProcuraCustoUnif(ProcuraMelhorPrim):
    
    def __init__(self):
        super().__init__(AvaliadorCustoUnif())