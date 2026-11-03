# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 12

def simular_resfriamento_motor():
    # Parâmetros iniciais fornecidos no enunciado[cite: 1]
    t_atual = 95.0       # Temperatura inicial do motor em °C[cite: 1]
    t_amb = 25.0         # Temperatura ambiente em °C[cite: 1]
    k_term = 0.08        # Constante de resfriamento em min^-1[cite: 1]
    minutos = 0          # Contador de tempo em minutos
    
    # Critério de parada: a diferença em relação à temperatura ambiente deve ser menor que 0.5 °C (T <= 25.5 °C)[cite: 1]
    while (t_atual - t_amb) >= 0.5:
        # Computa a temperatura para o próximo minuto utilizando a fórmula de decaimento exponencial[cite: 1]
        t_atual = t_atual - k_term * (t_atual - t_amb)
        minutos += 1
        
    # Exibição do resultado final formatado
    print(f"Número de minutos decorridos: {minutos} min | Temperatura final calculada: {t_atual:.2f} °C")

# Execução da função
if __name__ == "__main__":
    simular_resfriamento_motor()