from sae.ambiente.elemento import Elemento

"""
O mecanismo de deliberação é responsável por gerar e selecionar os objetivos
a serem alcançados pelo agente. Ele utiliza o modelo do mundo para identificar os estados
que representam alvos e ordena-os de acordo com a distância até eles.
O objetivo é escolher os alvos mais próximos para que o agente possa agir de forma eficiente.
"""
class MecDelib:
    
    #Inicializa o modelo do mundo
    def __init__(self, modelo_mundo):
        self.__modelo_mundo = modelo_mundo
        self.__estado_inicial = None

    """
    Deliberar é gerar e selecionar os objetivos a serem alcançados pelo agente.
    Este método utiliza os métodos privados da classe para chegar aos objetivos.
    """
    def deliberar(self):
        objetivos = self.__gerar_objetivos()
        if self.__estado_inicial is None:
            self.__estado_inicial = self.__modelo_mundo.obter_estado()
        if objetivos:
            return self.__selecionar_objetivos(objetivos)
        else:
            return [self.__estado_inicial]

    """
    Este método é um gerador, ou seja, ele gera uma lista de estados, que representam
    objetivos no modelo do mundo. Itera sobre todos os estados do modelo e verifica se o elemento
    correspondente é um alvo. Se for, o estado é adicionado à lista de objetivos.
    """
    def __gerar_objetivos(self):
        return [estado for estado in self.__modelo_mundo.obter_estados()
                if self.__modelo_mundo.obter_elemento(estado) == Elemento.ALVO]

    """
    O método __selecionar_objetivos ordena os objetivos de acordo com a distância
    até eles, utilizando o modelo do mundo. A lista de objetivos é ordenada em ordem
    crescente de distância, e o método retorna a lista ordenada.
    Isso garante que os objetivos mais próximos sejam priorizados na deliberação.
    Utilizamos como key a função de distância passada como objeto.
    """
    def __selecionar_objetivos(self, objetivos):
        objetivos.sort(key=self.__modelo_mundo.distancia)
        return objetivos