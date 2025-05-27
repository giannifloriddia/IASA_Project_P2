from lib.pdm.pdm import PDM
from lib.pdm.modelo.modelo_pdm import ModeloPDM

"""
Criamos um modelo de PDM para o ambiente 7x1,
detalhado no pdf 15-pds-exemplo
Em que temos um array com 7 estados,
e duas ações possíveis: '<' e '>',
consideramos os estados 1 e 7 como estados terminais.
"""
class ModeloAmbiente7x1(ModeloPDM):

    def __init__(self):
        #conjunto de estados do mundo
        self.__S = [1, 2, 3, 4, 5, 6, 7]
        #acões possíveis no estado s
        self.__A = ['<', '>']
        #probabilidades de transição de um estado aplicando uma ação
        self.__T = {
            (1, '<', 1): 0,
            (1, '>', 2): 0,
            (2, '<', 1): 1,
            (2, '>', 3): 1,
            (3, '<', 2): 1,
            (3, '>', 4): 1,
            (4, '<', 3): 1,
            (4, '>', 5): 1,
            (5, '<', 4): 1,
            (5, '>', 6): 1,
            (6, '<', 5): 1,
            (6, '>', 7): 1,
            (7, '<', 6): 0,
            (7, '>', 7): 0
        }
        #recompensa esperada na transição de um estado aplicando uma ação
        self.__R = {
            (1, '<', 1): 0,
            (1, '>', 2): 0,
            (2, '<', 1): -1,
            (2, '>', 3): 0,
            (3, '<', 2): 0,
            (3, '>', 4): 0,
            (4, '<', 3): 0,
            (4, '>', 5): 0,
            (5, '<', 4): 0,
            (5, '>', 6): 0,
            (6, '<', 5): 0,
            (6, '>', 7): 1,
            (7, '<', 6): 0,
            (7, '>', 7): 0
        }
        #Transições possíveis
        self.__transicoes = {
            (s, a): sn
            for (s, a, sn) in self.__T
            if s not in [1, 7]
            #estado, acao : estados seguintes na chave do dicionario de t
            #se o estado atual não for terminal
        }

    # Retorna o conjunto de estados do mundo
    def S(self):
        return self.__S

    """
    Retorna uma lista vazia se o estado for terminal,
    ou a lista de ações possíveis se não for
    """
    def A(self, s):
        return self.__A if s not in [1, 7] else []

    #Retorna a probabilidade de transição de um estado s para sn através da ação a
    def T(self, s, a, sn):
        return self.__T.get((s, a, sn))

    #Retorna a recompensa esperada na transição de um estado s para sn através da ação a
    def R(self, s, a, sn):
        return self.__R.get((s, a, sn))

    """
    Gera o estado sucessor que resulta de aplicar a acção a no estado s
    """
    def suc(self, s, a):
        if (s, a) in self.__transicoes: # verifica se a transição existe
            sn = self.__transicoes.get((s, a)) #get para retornar None em vez de exceção
        return [sn] if sn else []
    
if __name__ == "__main__":
    """
    Testamos o PDM com o modelo do ambiente 7x1.
    O resultado esperado dá como esperado.
    """
    modelo = ModeloAmbiente7x1()
    pdm = PDM(modelo, 0.5, 0.0)
    utilidade, politica = pdm.resolver()
    print("\nUtilidade:", utilidade)
    print("\nPolítica:", politica, "\n")