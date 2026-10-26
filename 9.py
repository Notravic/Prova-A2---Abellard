# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 9

import math

def calcular_tensao_rms():
    # Lista de amostras instantâneas de tensão fornecida no enunciado
    amostras = [0.0, 110.0, 190.5, 220.0, 190.5, 110.0, 0.0, -110.0, -190.5, -220.0, -190.5, -110.0]
    
    # Número total de amostras (N)
    n = len(amostras)
    
    # Variável acumuladora para a soma dos quadrados das tensões
    soma_quadrados = 0.0
    for v in amostras:
        soma_quadrados += v ** 2
        
    # Cálculo da média quadrática e da raiz quadrada (V_RMS)
    v_rms = math.sqrt(soma_quadrados / n)
    
    # Exibição do resultado formatado conforme a saída esperada
    print(f"Amostras: {n} | V_RMS Calculado: {v_rms:.2f} V")

# Execução da função
if __name__ == "__main__":
    calcular_tensao_rms()
    