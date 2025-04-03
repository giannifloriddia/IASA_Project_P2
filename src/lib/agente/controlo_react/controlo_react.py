"""
Implementa o processamento interno
do agente que relaciona a percecao com a acao.
Implementa a "inteligencia do agente"

Num comportamento composto, uma percepção pode ativar várias reações, 
resultando em diferentes ações. O desafio é escolher qual ação executar.
Esta classe implementa essa seleção de ação, que pode ser feita de várias formas: 

Seleção de Ação:
- Hierarquia: Os comportamentos seguem uma hierarquia fixa onde uns 
              podem suprimir ou substituir outros.  
- Prioridade: As respostas são escolhidas com base numa prioridade que 
              pode mudar durante a execução.  
- Combinação: As respostas podem ser combinadas numa única ação, por exemplo, 
              através da soma vetorial. (Não implementamos este algoritmo na disciplina).
"""
class ControloReact:

    #Construtor da classe
    def __init__(self, comportamento):
        self.__comportamento = comportamento
    
    """
    Ativa o comportamento de acordo com a perceção
    recebida e retorna uma ação.
    """
    def processar(self, percecao):
        return self.__comportamento.ativar(percecao)