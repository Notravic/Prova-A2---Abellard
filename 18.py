# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 18

def analisar_desbalanceamento_alimentadores():
    # Lista de dicionários contendo os dados dos 3 alimentadores industriais[cite: 1]
    alimentadores = [
        {"id": "Alimentador 1", "fases": [115.0, 114.0, 116.0]},
        {"id": "Alimentador 2", "fases": [140.0, 138.0, 142.0]},
        {"id": "Alimentador 3", "fases": [90.0, 125.0, 88.0]}
    ]
    
    # Itera sobre a lista de alimentadores[cite: 1]
    for alt in alimentadores:
        fases = alt["fases"]
        i_medio = sum(fases) / len(fases)
        
        # Encontra o maior desvio absoluto em relação à média
        max_desvio = max(abs(f - i_medio) for f in fases)
        
        # Calcula o percentual de desbalanceamento[cite: 1]
        desbalanceamento_pct = (max_desvio / i_medio) * 100.0
        
        # Avalia o critério regulatório (limite de 15.0%)[cite: 1]
        if desbalanceamento_pct > 15.0:
            alt["status"] = "ALERTA_DESBALANCEAMENTO"
        else:
            alt["status"] = "CONFORME"
            
        alt["desbalanceamento_pct"] = desbalanceamento_pct
        
        # Exibição dos resultados formatados
        print(f"{alt['id']} -> Desbalanceamento: {desbalanceamento_pct:.2f}% | Status: {alt['status']}")

# Execução da função
if __name__ == "__main__":
    analisar_desbalanceamento_alimentadores()