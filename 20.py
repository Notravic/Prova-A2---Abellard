# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 20

def sistema_deslastre_cargas():
    # Lista de dicionários representando os circuitos industriais[cite: 1]
    cargas = [
        {"circuito": "UTI_HOSPITALAR", "corrente_a": 60.0, "prioridade": 1, "ligado": True},
        {"circuito": "ILUMINACAO_PUBLICA", "corrente_a": 45.0, "prioridade": 3, "ligado": True},
        {"circuito": "BOMBEAMENTO_ESGOTO", "corrente_a": 55.0, "prioridade": 2, "ligado": True},
        {"circuito": "CLUBE_RECREATIVO", "corrente_a": 35.0, "prioridade": 4, "ligado": True}
    ]
    
    # Corrente máxima admissível do transformador (A)[cite: 1]
    corrente_maxima = 150.0
    
    print("--- Estado Inicial das Cargas ---")
    corrente_total = sum(c["corrente_a"] for c in cargas if c["ligado"])
    print(f"Corrente total inicial: {corrente_total} A (Limite: {corrente_maxima} A)")
    
    # Ordena as cargas da menor prioridade (4) para a maior prioridade (1)
    cargas_ordenadas = sorted(cargas, key=lambda x: x["prioridade"], reverse=True)
    
    print("\n--- Iniciando Processo de Deslastre ---")
    # Desliga cargas progressivamente enquanto a corrente total exceder o limite admissível
    for carga in cargas_ordenadas:
        if corrente_total <= corrente_maxima:
            break
            
        if carga["ligado"]:
            carga["ligado"] = False
            corrente_total -= carga["corrente_a"]
            print(f"DESLARGUE ATIVADO: Circuito '{carga['circuito']}' desligado. Nova corrente total: {corrente_total} A")
            
    print("\n--- Estado Final dos Circuitos ---")
    for c in cargas:
        estado = "LIGADO" if c["ligado"] else "DESLIGADO"
        print(f"Circuito: {c['circuito']} | Corrente: {c['corrente_a']} A | Prioridade: {c['prioridade']} | Status: {estado}")

# Execução da função
if __name__ == "__main__":
    sistema_deslastre_cargas()