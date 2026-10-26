# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 3

def calcular_rendimento_transformador():
    # Entradas de teste especificadas no enunciado
    p_saida_kw = 450.0  # Potência de saída em kW[cite: 1]
    p_nucleo_w = 1200.0 # Perdas magnéticas no núcleo em Watts[cite: 1]
    p_cobre_w = 3800.0  # Perdas ôhmicas no enrolamento em Watts[cite: 1]
    
    # Conversão das perdas de Watts para quilowatts (kW) para manter a coerência dimensional
    p_nucleo_kw = p_nucleo_w / 1000.0
    p_cobre_kw = p_cobre_w / 1000.0
    
    # Cálculo da potência de entrada total em kW
    p_entrada_kw = p_saida_kw + p_nucleo_kw + p_cobre_kw
    
    # Cálculo do rendimento percentual (eta)
    rendimento_percentual = (p_saida_kw / p_entrada_kw) * 100.0
    
    # Exibição do resultado formatado com precisão de três casas decimais
    print(f"Potência de Entrada: {p_entrada_kw:.3f} kW | Rendimento: {rendimento_percentual:.3f} %")

# Execução da função
if __name__ == "__main__":
    calcular_rendimento_transformador()