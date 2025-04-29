from modelo.heuristica_contagem import HeuristicaContagem
from modelo.problema_contagem import ProblemaContagem
from pee.mec_proc.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_aa import ProcuraAA
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
valor_final = 20
incrementos = [5, 1, 9, 4, 5]

# Criamo o problema e escolhemos um mecanismo de procura
problema = ProblemaContagem(valor_inicial, valor_final, incrementos)
mec_proc = ProcuraProfundidade()

# A solução é encontrada através do método procurar do mecanismo de procura
solucao = mec_proc.procurar(problema)

#Prints para verificar a solução encontrada
if solucao:
    print("Procura em profundidade")
    print("Solução encontrada!")
    print("-> Dimensão:", solucao.dimensao)
    print("-> Custo:", solucao.custo)
    print("Passos:")
    for passo in solucao:
        print("- Estado:", passo.estado.valor)
        print("- Operador:", passo.operador.incremento)
        print("------------------------")

    print("Observamos que o a dimensão da solução é:", solucao.dimensao, 
        "E o custo da solução é:", solucao.custo)
    print("------------------------------------")

mec_proc = ProcuraLargura()
solucao = mec_proc.procurar(problema)

#Prints para verificar a solução encontrada
if solucao:
    print("Procura em largura")
    print("Solução encontrada!")
    print("-> Dimensão:", solucao.dimensao)
    print("-> Custo:", solucao.custo)
    print("Passos:")
    for passo in solucao:
        print("- Estado:", passo.estado.valor)
        print("- Operador:", passo.operador.incremento)
        print("------------------------")

    print("Observamos que o a dimensão da solução é:", solucao.dimensao, "E o custo da solução é:", solucao.custo)
    print("Ou seja, a dimensão diminuiu em comparação ao mecanismo de procura em profundidade," \
    " porém, o custo foi quase o dobro.")
    print("------------------------------------")

mec_proc = ProcuraCustoUnif()
solucao = mec_proc.procurar(problema)

#Prints para verificar a solução encontrada
if solucao:
    print("Procura Custo Uniforme")
    print("Solução encontrada!")
    print("-> Dimensão:", solucao.dimensao)
    print("-> Custo:", solucao.custo)
    print("Passos:")
    for passo in solucao:
        print("- Estado:", passo.estado.valor)
        print("- Operador:", passo.operador.incremento)
        print("------------------------")

    print("Observamos que o a dimensão da solução é:", solucao.dimensao, "E o custo da solução é:", solucao.custo)
    print("Encontramos assim a solução com menor dimensão e custo, porém, tal como os " \
    "algoritmos usados até agora, não tira partido de conhecimento do domínio do problema")
    print("------------------------------------")
    print("O resto ainda não funciona mas na proxima aula está resolvido")

heuristica = HeuristicaContagem(valor_final)
heuristica = HeuristicaContagem(valor_final)
mec_proc = ProcuraAA()
solucao = mec_proc.procurar(problema)

#Prints para verificar a solução encontrada
if solucao:
    print("Procura AA")
    print("Solução encontrada!")
    print("-> Dimensão:", solucao.dimensao)
    print("-> Custo:", solucao.custo)
    print("Passos:")
    for passo in solucao:
        print("- Estado:", passo.estado.valor)
        print("- Operador:", passo.operador.incremento)
        print("------------------------")

    print("Observamos que o a dimensão da solução é:", solucao.dimensao, "E o custo da solução é:", solucao.custo)
    print("Encontramos assim a solução com menor dimensão e custo, porém, tal como os " \
    "algoritmos usados até agora, não tira partido de conhecimento do domínio do problema")
    print("------------------------------------")