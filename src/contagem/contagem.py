from modelo.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_prof_iter import ProcuraProfIter

"""
Neste package modelo, definimos um problema específico, neste caso, o problema de contagem.
Para isso, teremos de definir o problema, o estado e o operador, usando já, o modelo criado.
O problema consiste em contar a partir de um valor inicial até um valor final,
utilizando incrementos definidos. 
"""

valor_inicial = 0
valor_final = 9
incrementos = [2, 1]

# Criamo o problema e escolhemos um mecanismo de procura
problema = ProblemaContagem(valor_inicial, valor_final, incrementos)
mec_proc = ProcuraProfIter()

# A solução é encontrada através do método procurar do mecanismo de procura
solucao = mec_proc.procurar(problema)

#Prints para verificar a solução encontrada
if solucao:
    print("Solução encontrada!")
    print("-> Dimensão:", solucao.dimensao)
    print("-> Custo:", solucao.custo)
    print("Passos:")
    for passo in solucao:
        print("- Estado:", passo.estado.valor)
        print("- Operador:", passo.operador.incremento)
        print("------------------------")