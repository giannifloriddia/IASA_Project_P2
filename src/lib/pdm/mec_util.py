"""
O mecanismo de utililidade serve somente
para calcular matematicamente a utilidade dos
estados e de uma ação.
"""
class MecUtil:

    #Inicializamos as variáveis necessárias
    def __init__(self, modelo, gama, delta_max):
        self.__modelo = modelo
        self.__delta_max = delta_max
        self.__gama = gama

    """
    A utilidade U(s) representa o valor esperado de estar num estado s, 
    assumindo que se segue uma política de ações. Esta utilidade reflete 
    os ganhos acumulados ao longo do tempo, ou seja, a soma das recompensas 
    futuras ao seguir uma determinada sequência de decisões. Para evitar que 
    esta soma seja infinita, usa-se um fator de desconto gama entre [0,1], 
    que dá mais peso às recompensas imediatas e menos às futuras, resultando 
    numa utilidade descontada.

    O uso do fator de desconto resolve dois problemas: impede que a utilidade cresça 
    indefinidamente em ciclos positivos e assegura que recompensas mais próximas no 
    tempo sejam mais valiosas, refletindo decisões mais realistas.

    Para o cálculo da utilidade ótima, utilizamos o método de iteração de valores,
    que é um processo iterativo onde a utilidade de cada estado é atualizada
    repetidamente até que a diferença entre iterações sucessivas seja menor
    que um valor de tolerância (delta_max). Este método é eficiente para
    encontrar a utilidade mesmo em ambientes complexos.
    """
    def utilidade(self):
        """
        Fazemos uma atribuição por referência,
        para podermos simplificar o código.
        """
        S, A = self.__modelo.S, self.__modelo.A
        U = {s: 0 for s in S()}
        while True:
            Uant = U.copy()
            delta = 0
            for s in S():
                U[s] = max([self.util_acao(s, a, Uant) for a in A(s)], default=0)
                delta = max(delta, abs(U[s] - Uant[s]))
            if delta <= self.__delta_max:
                break
        return U

    """
    Esta função aplica a equação de Bellman para calcular o valor 
    de uma ação num determinado estado, ponderando as probabilidades 
    de transição, as recompensas imediatas, e a utilidade futura 
    descontada dos estados seguintes. 
    """
    def util_acao(self, s, a, U):
        T, R, suc = self.__modelo.T, self.__modelo.R, self.__modelo.suc
        return sum(T(s, a, sn) * (R(s, a, sn) + self.__gama * U[sn]) for sn in suc(s, a))