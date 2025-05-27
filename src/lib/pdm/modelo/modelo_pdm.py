from abc import ABC, abstractmethod

"""
Um Processo de Decisão de Markov (PDM) modela decisões em ambientes com incerteza. A cada momento, 
o agente está num estado e escolhe uma ação, que pode levar a vários 
estados seguintes, cada um com uma probabilidade e uma recompensa 
associada. Esta incerteza nas transições é o que caracteriza um 
processo não determinista.

A propriedade de Markov garante que a decisão depende apenas do 
estado atual, e não do caminho percorrido até lá. Ou seja, a 
previsão do futuro só precisa de saber o presente.

Um PDM é definido por:
- S: conjunto de estados
- A(s): ações possíveis no estado s
- T(s, a, s'): probabilidade de transição de s para s' com a
- R(s, a, s'): recompensa esperada ao fazer essa transição

O objetivo é escolher ações que maximizem a utilidade esperada a longo prazo, 
mesmo que o resultado imediato não seja sempre o melhor.
"""
class ModeloPDM(ABC):
    
    @abstractmethod
    def S(self):
        """
        conjunto de estados do mundo
        """

    @abstractmethod
    def A(self, s):
        """
        conjunto de acções possíveis no estado s : S
        """

    @abstractmethod
    def T(self, s, a, sn):
        """
        probabilidade de transição de s para s' através de a
        """

    @abstractmethod
    def R(self, s, a, sn):
        """
        recompensa esperada na transição de s para s' através de a
        """

    @abstractmethod
    def suc(self, s, a):
        """
        estado sucessor de s através de a
        """