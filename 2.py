# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 2

import math

def converter_fasor_retangular_para_polar():
    # Entradas de teste especificadas no enunciado
    v_r = 127.0  # Parte real da tensão (V)
    v_i = -73.32 # Parte imaginária da tensão (V)
    
    # Cálculo da magnitude eficaz |V|
    magnitude_v = math.sqrt(v_r**2 + v_i**2)
    
    # Cálculo do ângulo de fase em graus utilizando math.atan2
    angulo_rad = math.atan2(v_i, v_r)
    angulo_deg = angulo_rad * (180.0 / math.pi)
    
    # Exibição do resultado formatado com duas casas decimais conforme a saída esperada
    print(f"Fasor Polar: |V| = {magnitude_v:.2f} V | Ângulo = {angulo_deg:.2f}°")

# Execução da função
if __name__ == "__main__":
    converter_fasor_retangular_para_polar()