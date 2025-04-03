from ecr.comportamento import Comportamento
from sae.agente.avancar import Avancar

"""
Sem memória, os comportamentos podem enfrentar problemas, como:  

- Exploração ineficiente: O agente pode repetir 
    trajetos já percorridos, desperdiçando tempo.  
- Ótimos locais: Pode ficar preso em certas áreas.  
- Movimentos repetitivos: Pode entrar em ciclos de movimento 
    sem sair do lugar.  

Por isso, uma arquitetura reativa com memória resolve isso porque as 
ações não dependem apenas das perceções atuais, 
mas também de informações anteriores. O sistema guarda um 
histórico das perceções e reações passadas, 
ajustando o comportamento com base nessa memória 
para evitar erros repetitivos e melhorar a eficiência.
"""
class ExplorarComMemoria(Comportamento):
    def __init__(self, size = 100):
        self.__memoria = []
        self.__size = size
    
    """
    É guardada a posição e direção do agente na memória.
    Se a situação já estiver na memória, não faz nada.
    Se não estiver, adiciona à memória e retorna a ação de avançar.
    A memória tem um tamanho máximo, e quando atinge esse limite,
    remove o elemento mais antigo.
    Isso garante que a memória não cresça indefinidamente e
    consoma muita memória.
    """
    def ativar(self, percecao):
        situacao = percecao.posicao, percecao.direccao
        if situacao not in self.__memoria:
            self.__memoria.append(situacao)
            if len(self.__memoria) > self.__size:
                self.__memoria.pop(0)
            return Avancar()
