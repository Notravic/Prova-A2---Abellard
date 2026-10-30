# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 10

def calcular_consumo_e_tarifacao():
    # Lista de 24 leituras horárias de potência média consumida em kW
    demanda_24h = [
        40, 38, 35, 36, 42, 55, 70, 85, 90, 92, 88, 86, 
        84, 87, 91, 95, 110, 135, 150, 145, 130, 95, 65, 48
    ]
    
    # Tarifas definidas
    tarifa_fora_ponta = 0.65  # R$ / kWh
    tarifa_ponta = 1.85       # R$ / kWh
    delta_t = 1.0             # Intervalo de tempo em horas (1 h)
    
    consumo_total_kwh = 0.0
    custo_total = 0.0
    
    # Laço iterativo para percorrer cada hora (índice e valor da demanda)
    for i, potencia in enumerate(demanda_24h):
        # Energia consumida nesta hora (kWh)
        energia_hora = potencia * delta_t
        consumo_total_kwh += energia_hora
        
        # Aplicação da tarifa correspondente (Horário de Ponta nos índices 18, 19 e 20)
        if i in [18, 19, 20]:
            custo_total += energia_hora * tarifa_ponta
        else:
            custo_total += energia_hora * tarifa_fora_ponta
            
    # Exibição do resultado formatado conforme a saída esperada
    print(f"Consumo Total: {consumo_total_kwh:.2f} kWh | Custo Total: R$ {custo_total:.2f}")

# Execução da função
if __name__ == "__main__":
    calcular_consumo_e_tarifacao()