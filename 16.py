# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 16

import math

def processar_imutabilidade_e_fasor():
    # 1. Criação da tupla imutável com os dados de placa do transformador (V1, V2, S_nom, Z%)[cite: 1]
    trafo_placa = (13800.0, 220.0, 500.0, 4.5)
    print(f"Dados originais de placa (tupla): {trafo_placa}")
    
    # 2. Tentativa de alteração dinâmica protegida por bloco try / except TypeError[cite: 1]
    try:
        # As tuplas em Python não suportam atribuição de itens, o que gera um TypeError
        trafo_placa[2] = 750.0
    except TypeError as e:
        print(f"ERRO CAPTURADO: {e}")
        print("SEGURANÇA ATIVADA: Bloqueio comprovado de sobreescrita de placa! Os parâmetros do IED são imutáveis.")
        
    # 3. Função para cálculo do fasor polar de corrente a partir da forma retangular
    def calcular_fasor_corrente(i_r: float, i_i: float) -> tuple:
        # Cálculo da magnitude eficaz da corrente
        mag_i = math.sqrt(i_r**2 + i_i**2)
        # Cálculo do ângulo de fase em graus
        ang_i = math.atan2(i_i, i_r) * (180.0 / math.pi)
        # Retorna uma tupla imutável empacotada
        return (mag_i, ang_i)
        
    # Entrada de teste para o fasor de corrente retangular (ex: I_r = 10.0 A, I_i = 10.0 A)
    i_real, i_imag = 10.0, 10.0
    
    # Executa a função e faz o desempacotamento do resultado em duas variáveis isoladas[cite: 1]
    magnitude_polar, angulo_polar = calcular_fasor_corrente(i_real, i_imag)
    
    print(f"\nFasor polar de corrente desempacotado com sucesso:")
    print(f"Magnitude = {magnitude_polar:.2f} A | Ângulo = {angulo_polar:.2f}°")

# Execução da função
if __name__ == "__main__":
    processar_imutabilidade_e_fasor()