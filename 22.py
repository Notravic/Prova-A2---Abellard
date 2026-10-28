# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 22

import numpy as np

def calculo_fasorial_numpy():
    # 1. Definição dos fasores de tensão utilizando a forma de Euler (V * exp(j * radianos))
    v_a = 220.0 * np.exp(1j * np.radians(0.0))
    v_b = 220.0 * np.exp(1j * np.radians(-120.0))
    v_c = 220.0 * np.exp(1j * np.radians(120.0))
    
    # Criação do array 1D de tensões complexas
    v_dot = np.array([v_a, v_b, v_c], dtype=np.complex128)
    
    # 2. Definição do array de impedâncias complexas desbalanceadas das cargas (Z_A, Z_B, Z_C)
    z_dot = np.array([10.0 + 2.0j, 12.0 + 5.0j, 8.0 - 3.0j], dtype=np.complex128)
    
    # 3. Cálculo vetorial da Lei de Ohm fasorial (I_dot = V_dot / Z_dot) sem laço for
    i_dot = v_dot / z_dot
    
    # 4. Extração dos módulos e dos ângulos em graus (convertendo para float nativo do Python)
    modulos_i = [round(float(m), 2) for m in np.abs(i_dot)]
    angulos_i = [round(float(a), 1) for a in np.angle(i_dot, deg=True)]
    
    # Exibição dos resultados
    print(f"Módulos das Correntes: {modulos_i} A")
    print(f"Ângulos de Fase: {angulos_i}°")

# Execução da função
if __name__ == "__main__":
    calculo_fasorial_numpy()