from modelo.heuristica_contagem import HeuristicaContagem
from modelo.problema_contagem import ProblemaContagem
from pee.melhor_prim.procura_custo_unif import ProcuraCustoUnif
from pee.melhor_prim.procura_aa import ProcuraAA
from pee.melhor_prim.procura_sofrega import ProcuraSofrega
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

# Criamo o problema e a heurística, e escolhemos um mecanismo de procura
problema = ProblemaContagem(valor_inicial, valor_final, incrementos)
heuristica = HeuristicaContagem(valor_final)

def print_solution(mecanismo_proc):

    print("-----------------------------------")

    if isinstance(mecanismo_proc, ProcuraAA) or isinstance(mecanismo_proc, ProcuraSofrega):
        solucao_atual = mecanismo_proc.procurar(problema, heuristica)
    else:
        solucao_atual = mecanismo_proc.procurar(problema)

    if solucao_atual:
        print(mecanismo_proc, "\n")

        print("-> Dimensão:", solucao_atual.dimensao)
        print("-> Custo:", solucao_atual.custo, "\n")

        print("->Nº nós processados:", mecanismo_proc.nos_processados)
        print("->Nº nós máx em memória:", mecanismo_proc.nos_em_memoria, "\n")        

        print("Passos:")
        for passo in solucao_atual:
            print("- Estado:", passo.estado.valor)
            print("- Operador:", passo.operador.incremento)
            print("------------------------")

print_solution(ProcuraProfundidade())
print("Na procura em profundidade, seguimos sempre o " \
"caminho mais fundo possível antes de voltar atrás. Neste caso, " \
"encontramos uma solução com custo 100, mas que não é ótima, " \
"porque este tipo de procura ignora os custos dos ramos. Processou " \
"21 nós e manteve-os todos em memória. Apesar de ter chegado " \
"a uma solução, poderia ter escolhido um caminho bem mais barato se " \
"usasse outro método, como a procura com custo uniforme.")

print_solution(ProcuraLargura())
print("Na procura em largura, exploramos primeiro todos os nós ao " \
"mesmo nível antes de avançar para o seguinte. Isso garante que encontramos " \
"a solução com o menor número de passos, mas não necessariamente a mais barata. " \
"Aqui, apesar de a solução ser válida, teve um custo de 187, bem maior que na profundidade "
"(100), e precisou de 216 nós em memória, contra apenas 21 na Procura em Profundidade. " \
"Ou seja, a procura em largura é mais completa, mas consome bem mais memória e, tal " \
"como a profundidade, não considera os custos dos caminhos.")

print_solution(ProcuraProfLim())
print("A procura em profundidade limitada é igual à em profundidade, mas com " \
"um limite na profundidade dos nós. Neste caso, o limite não impediu de encontrar " \
"a mesma solução do mecanismo original, com custo 100 e 21 nós processados e em memória. " \
"Assim como antes, não encontra a solução ótima, mas já é mais segura, porque evita " \
"ir muito fundo em ciclos ou caminhos longos.")

print_solution(ProcuraProfIter())
print("A procura em profundidade iterativa combina o baixo uso de memória da procura " \
"em profundidade com a completude da procura em largura. Vai aumentando o limite de " \
"profundidade aos poucos, repetindo a busca. Aqui, encontrou a mesma solução que a largura, " \
"com custo 187, mas processando muito menos nós (26 vs 216) e com menos memória (12 vs 216). " \
"Ainda assim, tal como as anteriores, ignora os custos dos caminhos, por isso também não encontrou a solução ótima.")

print_solution(ProcuraCustoUnif())
print("Ao contrário das outras procuras, a custo uniforme considera os custos dos ramos e garante " \
"sempre a solução ótima. Neste caso, encontrou o caminho com custo 20, muito melhor que os 100 ou 187 " \
"das outras abordagens. No entanto, processou 126 nós e manteve 76 em memória, o que é mais do que a " \
"profundidade mas menos que a largura. Ou seja, é mais eficiente em termos de custo, mas pode ser mais " \
"pesada dependendo do problema, é ideal quando o custo importa mesmo.")

print_solution(ProcuraSofrega())
print("A procura sofrega usa uma heurística para escolher o próximo nó, " \
"tentando chegar rapidamente ao objetivo. No entanto, só olha para a estimativa até ao objetivo e " \
"ignora o custo acumulado, o que pode levar a escolhas pouco eficientes. " \
"Aqui, apesar de ter usado menos memória (17 nós) e processado apenas 21, acabou com um custo bem mais " \
"alto (164). Foi mais rápida, mas neste caso ficou longe de ser ótima — mostra " \
"o risco de seguir apenas a heurística sem considerar os custos reais.")

print_solution(ProcuraAA())
print("A procura A* junta o melhor da custo uniforme e da sofrega: considera o custo acumulado " \
"como a custo uniforme, e também usa uma heurística como a sofrega. Por isso, consegue encontrar a " \
"solução ótima, como se vê aqui com o custo 20.0, igual ao da custo uniforme, mas com menos nós processados "
"(101 vs 126). Em troca, usou um pouco mais de memória (81 nós), " \
"mas de forma eficiente.")

#Testar com novos parâmetros
valor_inicial = 0
valor_final = 9
incrementos = [1, 2, -1]

# Criamo o problema e a heurística, e escolhemos um mecanismo de procura
problema = ProblemaContagem(valor_inicial, valor_final, incrementos)
heuristica = HeuristicaContagem(valor_final)

mecanismos = [ProcuraLargura(), ProcuraProfLim(5), ProcuraProfIter(5), ProcuraCustoUnif(), ProcuraSofrega(), ProcuraAA() ]

print("\n-------------------|Novo problema|-------------------")
for mecanismo in mecanismos:
    print_solution(mecanismo)
    if mecanismo in mecanismos[3:]:
        print("Nº de nós repetidos:", mecanismo.contador)
print("Verificamos que todos os mecanismos estão a funcionar como o esperado")