from .comport_comp import ComportComp
"""
Lambda: função anonima que permite criar funções simples em uma linha.
Funções lambdas fazem somente transfomação de dados.
Retornar o maior elemento da lista de açoes, sendo que a chave de avaliação 
desses elementos é a prioridade de cada ação
"""
class Prioridade(ComportComp):
    def selecionar_acao(acoes):
        return max(acoes, key=lambda acao: acao.prioridade)