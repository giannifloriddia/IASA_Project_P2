from ..controlo_delib.mec_delib import MecDelib
from ..controlo_delib.modelo.modelo_mundo import ModeloMundo

"""
O controlo deliberativo, serve para decidir o que fazer, ou seja, 
o processo de deliberação. 
Dada uma perceção do ambiente, o componente ControloDelib tem a 
responsabilidade de processá-la e decidir a ação a ser executada.
"""
class ControloDelib:
    
    """
    Inicializa o modelo do mundo e o mecanismo de deliberação,
    para além de receber o planeador e inicializar um lista de
    objetivos e um plano.
    """
    def __init__(self, planeador):
        self.__modeloMundo = ModeloMundo()
        self.__mec_del = MecDelib(self.__modeloMundo)
        self.__planeador = planeador
        self.__objetivos = None
        self.__plano = None

    """
    O método processar serve para processar a perceção do ambiente,
    Primeiro assimila-a, e, se tiver de reconsiderar, delibera e planeia.
    Por fim, executa a ação correspondente ao plano.
    """
    def processar(self, percecao):
        self.__assimilar(percecao)
        if self.__reconsiderar():
            self.__deliberar()
            self.__planear()
        return self.__executar()

    """
    Assimilar é o processo de atualizar o modelo do mundo com a perceção recebida.
    """
    def __assimilar(self, percecao):
        self.__modeloMundo.atualizar(percecao)
        """return void"""

    """
    O método reconsidera, se o modelo do mundo foi alterado ou se o plano é nulo.
    """
    def __reconsiderar(self):
        return (self.__modeloMundo.alterado) or (self.__plano is None)

    """
    Delibera os objetivos a serem alcançados
    """
    def __deliberar(self):
        self.__objetivos = self.__mec_del.deliberar()

    """
    Planeia como alcançar os objetivos, se houver algum, através do planeador.
    """
    def __planear(self):
        if self.__objetivos:
            self.__plano = self.__planeador.planear(self.__modeloMundo, self.__objetivos)
        else:
            self.__plano = None

    """
    Executa a ação do plano, se houver algum. Se não houver plano, retorna None.
    Se houver plano, obtém o estado atual do modelo do mundo e tenta obter a ação
    correspondente ao estado atual. Se não houver ação, o plano é definido como None.
    """
    def __executar(self):
        if self.__plano:
            estado = self.__modeloMundo.obter_estado()
            operador = self.__plano.obter_acao(estado)
            if operador:
                return operador.acao
            else:
                self.__plano = None
    
    """
    Método para mostrar a vista com o modelo do mundo e o plano a ser executado no ambiente.
    """
    def mostrar(self, vista): #público (diferente da arquitetura)
        vista.limpar()
        self.__modeloMundo.mostrar(vista)
        if self.__plano:
            self.__plano.mostrar(vista)
        if self.__objetivos:
            for objetivo in self.__objetivos:
                vista.marcar_posicao(objetivo.posicao)