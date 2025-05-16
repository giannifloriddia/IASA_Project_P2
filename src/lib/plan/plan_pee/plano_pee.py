from plan.plano import Plano

"""
O plano pee é uma implementação do plano que contém uma lista de passos.
Um passo é uma ação a ser executada em um determinado estado.
Um passo é representado por um operador e um estado.
"""
class PlanoPEE(Plano):

    #Dimensão do plano (tamanho da lista de passos)
    @property
    def dimensao(self):
        return len(self.__passos)

    #Inicializa o plano com a lista de passos.
    def __init__(self, solucao):
        self.__passos = [passo for passo in solucao]

    """
    Vai retirar e retornar o primeiro passo da 
    lista de passos e verificar se o estado
    do passo é igual ao estado passado como
    parâmetro. Se for, retorna o operador associado.
    Obtendo assim, a ação/passo a ser executada.
    """
    def obter_acao(self, estado):
        if self.__passos:
            passo = self.__passos.pop(0)
            if passo.estado == estado:
                return passo.operador

    """
    Mostra os vetores do plano utilizando a vista da SAE.
    """
    def mostrar(self, vista):
        if self.__passos:
            for passo in self.__passos:
                vista.mostrar_vector(passo.estado.posicao, passo.operador.ang)