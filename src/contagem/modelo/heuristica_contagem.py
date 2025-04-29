from pee.melhor_prim.heuristica import Heuristica

class HeuristicaContagem(Heuristica):
    
    def __init__(self, valorfinal):
        super().__init__()
        self.__valorfinal = valorfinal

    def h(self, estado):
        #return abs(estado.contagem - self.__valorfinal)
        return abs(estado.id_valor() - self.__valor_final)