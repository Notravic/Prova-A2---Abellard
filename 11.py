# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 11

def varredura_telemetria_scada():
    # Vetor de correntes de fase fornecido no enunciado
    correntes = [82.0, 85.5, -99.0, 90.0, 94.2, -50.0, 105.0, 218.0, 95.0, 91.0]
    
    soma_correntes = 0.0
    quantidade_validas = 0
    
    for i in correntes:
        # Se a corrente for negativa, descarta a amostra com 'continue'
        if i < 0.0:
            print(f"RUÍDO_DESCARTADO: Amostra negativa detectada ({i} A).")
            continue
            
        # Se a corrente for superior a 200.0 A, interrompe imediatamente com 'break'
        elif i > 200.0:
            print(f"ALARME DE FALTA: Corrente crítica de {i} A detectada. Interrupção imediata do ciclo (TRIP).")
            break
            
        # Caso contrário, acumula para o cálculo da média
        else:
            soma_correntes += i
            quantidade_validas += 1
            
    # Cálculo e exibição da média das leituras válidas processadas antes do trip
    if quantidade_validas > 0:
        media_validas = soma_correntes / quantidade_validas
        print(f"Amostras válidas processadas: {quantidade_validas} | Média Calculada: {media_validas:.2f} A")

# Execução da função
if __name__ == "__main__":
    varredura_telemetria_scada()