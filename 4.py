# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 4

import math

def calcular_correcao_fator_potencia():
    # Entradas de teste especificadas no enunciado
    p = 320.0       # Potência ativa em kW[cite: 1]
    fp_atual = 0.80 # Fator de potência medido indutivo[cite: 1]
    fp_alvo = 0.92  # Fator de potência regulatório exigido pelo PRODIST[cite: 1]
    
    # Verifica se a correção é necessária (FP inferior ao limite regulatório)
    if fp_atual < fp_alvo:
        # Cálculo da potência reativa necessária (Q_c) em kVAr
        q_c = p * (math.tan(math.acos(fp_atual)) - math.tan(math.acos(fp_alvo)))
        
        # Exibição do resultado formatado conforme a saída esperada
        print(f"Potência Reativa Requerida (Qc): {q_c:.2f} kVAr")
    else:
        print("Fator de potência conforme as normas.")

# Execução da função
if __name__ == "__main__":
    calcular_correcao_fator_potencia()