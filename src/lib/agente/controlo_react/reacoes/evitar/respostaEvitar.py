from ecr.resposta import Resposta
from sae.agente.rodar import Rodar

class RespostaEvitar(Resposta):
    def ativar(self, percecao, intensidade):
        dir_atual = percecao.direccao
        if percecao.contacto_obst(dir_atual):
            nova_direcao = dir_atual.rodar()
            self._acao = Rodar(nova_direcao)
            return super().ativar(percecao, intensidade)
        
        #se na percecao houver indicacao de percecao 
        # com obst ela vai cria uma nova instancia de rodar 90 graus e depois altera o atributo acao com 
        # a nova instancia de rodar e depois invocar a superclasse