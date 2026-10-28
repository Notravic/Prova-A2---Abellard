# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 23

import numpy as np

def calculo_perdas_broadcasting():
    # Matriz de correntes de dimensão (4 x 3) para os 4 patamares horários e 3 fases (A, B, C)
    i_matriz = np.array([
        [80.0, 82.0, 81.0],
        [95.0, 94.0, 97.0],
        [120.0, 118.0, 122.0],
        [60.0, 59.0, 61.0]
    ])
    
    # Vetor 1D com as resistências dos condutores de cada fase em Ohms[cite: 1]
    r_fases = np.array([0.15, 0.15, 0.15])
    
    # 1. Cálculo da matriz de perdas instantâneas por efeito Joule utilizando broadcasting (P_perdas = I^2 * R)[cite: 1]
    p_perdas = (i_matriz ** 2) * r_fases
    
    # 2. Obtenção da perda total trifásica em Watts para cada um dos 4 patamares horários usando np.sum(axis=1)[cite: 1]
    perdas_trifasicas_hora = np.sum(p_perdas, axis=1)
    
    # Arredondamento para duas casas decimais (convertendo para float nativo)
    perdas_formatadas = [round(float(p), 2) for p in perdas_trifasicas_hora]
    
    # Exibição dos resultados formatados conforme a saída esperada[cite: 1]
    print(f"Perdas trifásicas por hora: {perdas_formatadas} W")

# Execução da função
if __name__ == "__main__":
    calculo_perdas_broadcasting()