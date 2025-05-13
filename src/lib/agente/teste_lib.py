from agente.controlo_delib.mec_delib import MecDelib
from plan.plan_pee.planeador_pee import PlaneadorPee
from sae.ambiente.ambiente import Ambiente
from sae.agente.transdutor import Transdutor
from sae.defamb import DEF_AMB
from controlo_delib.modelo.modelo_mundo import ModeloMundo
from agente.controlo_delib.modelo.estado_agente import EstadoAgente

"""
Neste módulo, realizamos testes para verificar se o modelo do mundo
está a funcionar corretamente. Utilizamos testes doctest para garantir
que as funções estão a retornar os resultados esperados.
"""

#Método para obter uma perceção
def obter_percecao():
    num_amb = 4
    ambiente = Ambiente(DEF_AMB[num_amb])
    transdutor = Transdutor()
    transdutor.iniciar(ambiente)
    return transdutor.percepcionar()

#Método para atualizar o modelo do mundo
def atualizar_modelo_mundo():
    """
    Testes de atualização do modelo do mundo.

    >>> modelo_mundo = atualizar_modelo_mundo()
    >>> modelo_mundo.alterado
    True

    >>> estado = modelo_mundo.obter_estado()
    >>> estado.posicao
    (0, 0)

    >>> estados = modelo_mundo.obter_estados()
    >>> len(estados)
    671

    >>> operadores = modelo_mundo.obter_operadores()
    >>> len(operadores)
    4

    >>> estado = EstadoAgente((28, 9))
    >>> modelo_mundo.obter_elemento(estado)
    <Elemento.ALVO: 'A'>
    """
    percecao = obter_percecao()
    modelo_mundo = ModeloMundo()
    modelo_mundo.atualizar(percecao)
    return modelo_mundo

def gerar_objetivos():
    """
    >>> objetivos = gerar_objetivos()
    >>> len(objetivos)
    3
    """
    modelo_mundo = atualizar_modelo_mundo()
    mec_delib = MecDelib(modelo_mundo)
    return mec_delib.deliberar()

def gerar_plano():
    """
    >>> plano = gerar_plano()
    >>> plano.dimensao
    37
    """
    planeador = PlaneadorPee()
    modelo_mundo = atualizar_modelo_mundo()
    objetivos = gerar_objetivos()
    return planeador.planear(modelo_mundo, objetivos)

"""
Verificamos se o nome do módulo é "__main__" para garantir que o código
só é executado quando o módulo é executado diretamente, e não quando é importado.
Utilizamos o módulo doctest para executar os testes definidos nas funções.
Os testes são definidos como docstrings nas funções e são executados
automaticamente quando o módulo é executado.
Se todos os testes passarem, não deveremos ver nenhuma mensagem de erro na consola.
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()