# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 1

def calcular_resistencia_termica():
    # Parâmetros físicos fornecidos
    rho_20 = 0.0282  # Resistividade do alumínio a 20 °C (ohm * mm^2 / m)
    alpha_20 = 0.0039  # Coeficiente térmico a 20 °C (°C^-1)
    
    # Entradas de teste especificadas no enunciado
    L_km = 12.5       # Comprimento em km
    S = 240.0         # Seção transversal em mm^2
    T = 45.0          # Temperatura de operação em °C
    
    # Conversão do comprimento de quilômetros para metros
    L_m = L_km * 1000.0
    
    # Aplicação da fórmula da Lei de Pouillet com correção térmica
    r_t = rho_20 * (L_m / S) * (1 + alpha_20 * (T - 20))
    
    # Exibição do resultado formatado conforme a saída esperada
    print(f"Resistência da linha a {T}°C: {r_t:.4f} ohms")

# Execução da função
if __name__ == "__main__":
    calcular_resistencia_termica()