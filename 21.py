# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 21

import math
from typing import Tuple

def queda_tensao_trifasica(
    i_linha: float, 
    comprimento_km: float, 
    fator_potencia: float, 
    r_km: float = 0.19, 
    x_km: float = 0.08
) -> Tuple[float, float, bool]:
    """
    Calcula a queda de tensão trifásica e a regulação percentual em linhas de transmissão.
    
    Parâmetros:
        i_linha (float): Corrente de linha em Amperes (A).
        comprimento_km (float): Comprimento da linha em quilómetros (km).
        fator_potencia (float): Fator de potência da carga (indutivo).
        r_km (float): Resistência linear em Ohms/km (padrão = 0.19).
        x_km (float): Reatância linear em Ohms/km (padrão = 0.08).
        
    Fórmula:
        delta_v = sqrt(3) * I * [R * FP + X * sin(arccos(FP))] * L
        Regulação (%) = (delta_v / 13800) * 100
        
    Retorna:
        Tuple[float, float, bool]: (Queda de Tensão em V, Regulação Percentual, Status de Conformidade <= 5.0%)
    """
    # Cálculo do seno do ângulo do fator de potência a partir do arccos(FP)
    seno_theta = math.sin(math.acos(fator_potencia))
    
    # Cálculo da queda de tensão em Volts (Delta V)
    delta_v = math.sqrt(3) * i_linha * (r_km * fator_potencia + x_km * seno_theta) * comprimento_km
    
    # Cálculo da regulação percentual para a base de 13800 V
    regulacao_percentual = (delta_v / 13800.0) * 100.0
    
    # Validação de conformidade regulatória (<= 5.0%)
    conforme = regulacao_percentual <= 5.0
    
    return (delta_v, regulacao_percentual, conforme)

# Execução com os dados de entrada de teste fornecidos no enunciado[cite: 1]
if __name__ == "__main__":
    i_teste = 120.0       # A[cite: 1]
    l_teste = 2.5         # km[cite: 1]
    fp_teste = 0.88       #[cite: 1]
    
    dv, reg, conf = queda_tensao_trifasica(i_teste, l_teste, fp_teste)
    
    print(f"ΔV = {dv:.2f} V, Regulação = {reg:.2f}% e Conforme: {conf}")