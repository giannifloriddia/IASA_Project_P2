from plan.plano import Plano

class PlanoPDM(Plano):
    
    def __init__(self, utilidade, politica):
        self.__utilidade = utilidade
        self.__politica = politica

    def obter_acao(self, estado):
        pass

    def mostar(self, vista):
        pass

#a recompensa de se atingir um objetivo é o valor rmax
#enquanto nao se atingir objetivo nao ha recompensa
#plano com mecanismopdm
