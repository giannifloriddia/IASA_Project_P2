"""
O mecanismo de utililidade serve somente
para calcular matematicamente a utilidade de um estado
e de uma ação.
"""
class MecUtil:

    #Inicializamos as variáveis necessárias
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__delta_max = delta_max
        self.__gama = gama

    """
    Calculamos a utilidade de um estado de acordo
    com o que estudamos, utilizando um delta máximo
    para parar o ciclo.
    """
    def utilidade(self):
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_acao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta < self.__delta_max:
                break
        return U

    """
    A utilidade da acção é calculada
    através da soma dos produtos
    entre a probabilidade de transição,
    a recompensa esperada e a utilidade
    do estado sucessor.
    """
    def util_acao(self, s, a, U):
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in suc(s, a))