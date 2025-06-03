from agente.controlo_delib.modelo.modelo_mundo import ModeloMundo
from plan.plano import Plano

class PlanoPDM(Plano):
    
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_acao(self, estado):
        if self.__politica:
            return self.__politica.get(estado)
        """"
        else:
            estado, _ = self.__politica.items()[0]
            print(estado.posicao)
            return self.__politica.get(estado)
        """

    def mostrar(self, vista):
        if self.__politica:
            #Mostrar utilidade
            for estado, valor in self.__utilidade.items(): #tuplo, parênteses implicitos
                vista.mostrar_valor_posicao(estado.posicao, valor)
            #Mostrar política
            for estado, acao in self.__politica.items():
                vista.mostrar_vector(estado.posicao, acao.ang)

#a recompensa de se atingir um objetivo é o valor rmax
#enquanto nao se atingir objetivo nao ha recompensa
#plano com mecanismopdm
