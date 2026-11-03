# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 13

def analisar_indicadores_alimentador():
    # Lista contendo 24 leituras horárias de demanda ativa em kW fornecida no enunciado[cite: 1]
    demanda_diaria = [
        42.0, 39.5, 38.0, 37.5, 41.0, 56.0, 72.0, 88.5, 94.0, 96.0, 91.5, 89.0,
        85.0, 88.0, 92.5, 98.0, 115.0, 142.0, 155.0, 148.5, 125.0, 98.0, 68.0, 50.0
    ]
    
    # 1. Fatiamento (slicing) para o turno da madrugada (00h às 05h, índices 0 a 5 inclusivos)
    turno_madrugada = demanda_diaria[0:6]
    
    # 2. Fatiamento com amostragem bi-horária (a cada 2 horas, passo = 2)
    amostragem_bihoraria = demanda_diaria[::2]
    
    # 3. Obtenção da demanda máxima e mínima
    p_maxima = max(demanda_diaria)
    p_minima = min(demanda_diaria)
    
    # Cálculo da demanda média diária
    p_media = sum(demanda_diaria) / len(demanda_diaria)
    
    # Cálculo do Fator de Carga diário (F_c = P_média / P_máxima)[cite: 1]
    fator_carga = p_media / p_maxima
    
    # Exibição dos resultados formatados conforme exigido
    print(f"Turno da Madrugada (00h-05h): {turno_madrugada}")
    print(f"Amostragem Bi-horária: {amostragem_bihoraria}")
    print(f"P_máx = {p_maxima:.1f} kW | P_mín = {p_minima:.1f} kW | Fator de Carga (F_c) = {fator_carga:.3f}")

# Execução da função
if __name__ == "__main__":
    analisar_indicadores_alimentador()