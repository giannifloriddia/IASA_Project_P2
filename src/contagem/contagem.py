from modelo.problema_contagem import ProblemaContagem
from pee.prof.procura_profundidade import ProcuraProfundidade
from pee.larg.procura_largura import ProcuraLargura
from pee.prof.procura_prof_lim import ProcuraProfLim
from pee.prof.procura_prof_iter import ProcuraProfIter

valor_inicial = 0
valor_final = 9
incrementos = [2,1]

problema = ProblemaContagem(valor_inicial, valor_final, incrementos)
mec_proc = ProcuraProfIter()
solucao = mec_proc.procurar(problema)

if solucao:
    print("Solução encontrada!")
    print("Dimensão:", solucao.dimensao)
    print("Custo:", solucao.custo)
    #print("Profundidade:", solucao.profundidade)
    print("Passos:")
    for passo in solucao:
        print("Estado:", passo.estado.valor)
        print("Operador:", passo.operador.incremento)
        print("------------------------")