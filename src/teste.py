#import sys

#print("------")
#print(sys.path)
#print("----")

from agente.agente_delib import AgenteDelib
from agente.agente_delib_pdm import AgenteDelibPDM
from sae import Simulador
from agente.agente_react import AgenteReact

#Criaçaõ de um simulador
#Criação de um agente reativo simples
#E execução do simulador

"""
agente = AgenteReact()
simulador = Simulador(1, agente)
simulador.executar()
"""

"""
#Testámos o agente deliberativo
agente = AgenteDelib()
simulador = Simulador(4, agente, vista_modelo=True)
simulador.executar()
"""

#Testámos também o agente deliberativo PDM
agente = AgenteDelibPDM()
simulador = Simulador(4, agente, vista_modelo=True)
simulador.executar()