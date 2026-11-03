# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 14

def buffer_circular_fifo():
    # Buffer inicial com capacidade estrita de 5 amostras[cite: 1]
    buffer = [81.2, 82.0, 80.9, 83.5, 82.8]
    
    # Novas leituras provenientes do conversor A/D[cite: 1]
    novas_leituras = [86.4, 91.0, 94.5]
    
    print(f"Buffer inicial: {buffer}")
    
    # Processa cada nova leitura recebida
    for leitura in novas_leituras:
        # Remove a amostra mais antiga (primeiro elemento) usando .pop(0)[cite: 1]
        buffer.pop(0)
        
        # Adiciona a nova leitura no final do buffer usando .append()[cite: 1]
        buffer.append(leitura)
        
        # Exibe o estado atual do buffer a cada ciclo[cite: 1]
        print(f"Nova amostra recebida ({leitura}) -> Estado do Buffer: {buffer}")

# Execução da função
if __name__ == "__main__":
    buffer_circular_fifo()