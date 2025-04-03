from ecr.resposta import Resposta
from sae.agente.rodar import Rodar

"""
Evita obstáculos rodando 90º.
Se na percecao houver indicacao de contacto 
com obstáculo, ela vai criar uma nova instancia 
de rodar 90 graus e depois altera o atributo acao com 
a nova instancia de rodar, e de seguida invoca a superclasse
"""
class RespostaEvitar(Resposta):
    def ativar(self, percecao, intensidade):
        dir_atual = percecao.direccao
        if percecao.contacto_obst(dir_atual):
            nova_direcao = dir_atual.rodar()
            self._acao = Rodar(nova_direcao)
            return super().ativar(percecao, intensidade)
        