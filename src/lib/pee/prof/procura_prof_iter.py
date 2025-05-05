from .procura_prof_lim import ProcuraProfLim

"""
A Procura em Profundidade Iterativa combina mais eficientemente 
os benefícios da procura em profundidade com as vantagens 
da procura em largura. Ela realiza sucessivas buscas em profundidade, 
cada vez com um limite de profundidade maior, mas sem guardar memória 
dos nós explorados entre cada iteração. Tal como a procura em profundidade 
limitada, permite controlar a profundidade máxima da procura, mantendo uma 
complexidade de memória linear. No entanto, tem uma vantagem importante: 
ao invés de exigir que a profundidade máxima seja previamente conhecida 
(como na procura em profundidade limitada), a profundidade iterativa vai 
ajustando esse limite dinamicamente, garantindo uma solução ótima 
como na procura em largura, mas com muito menos uso de memória.
"""
class ProcuraProfIter(ProcuraProfLim):

    """
    Este método recebe um problema de busca e dois parâmetros opcionais:
    - inc_prof: incremento da profundidade a cada iteração (padrão: 1).
    - limite_prof: profundidade máxima a ser explorada (padrão: 10).

    O método percorre os níveis de profundidade do problema começando em
    0 até o limite especificado, incrementando a profundidade em inc_prof
    a cada iteração. Para cada profundidade, ele chama o método de busca
    em profundidade limitada, passando o problema e atualizando a profundidade atual.
    Se uma solução é encontrada, ela é retornada. Caso contrário, o método
    continua a busca com uma profundidade maior até atingir o limite
    especificado. Se nenhuma solução for encontrada até o limite, o método
    retorna None por defeito.
    """
    def procurar(self, problema, inc_prof=1, limite_prof=10):
        for profundidade in range(0, limite_prof + 1, inc_prof):
            self._prof_max = profundidade
            solucao = super().procurar(problema)
            if solucao:
                return solucao
    
    """
    Alterei o método de representação da classe para facilidadede nos prints
    """
    def __repr__(self):
        return "Procura em Profundidade Iterativa"