# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 19

import json

def serializar_dados_json():
    # Estrutura de dados dos alimentadores processados no Exercício 18[cite: 1]
    alimentadores_subestacao = [
        {
            "id": "Alimentador 1", 
            "fases": [115.0, 114.0, 116.0],
            "desbalanceamento_pct": 0.87,
            "status": "CONFORME"
        },
        {
            "id": "Alimentador 2", 
            "fases": [140.0, 138.0, 142.0],
            "desbalanceamento_pct": 1.43,
            "status": "CONFORME"
        },
        {
            "id": "Alimentador 3", 
            "fases": [90.0, 125.0, 88.0],
            "desbalanceamento_pct": 23.77,
            "status": "ALERTA_DESBALANCEAMENTO"
        }
    ]
    
    # Serialização da estrutura de dados para uma string JSON (MQTT/IoT)
    # Utiliza indent=2 para formatação legível e ensure_ascii=False para suportar acentuação em português[cite: 1]
    pacote_json = json.dumps(alimentadores_subestacao, indent=2, ensure_ascii=False)
    
    print("--- Pacote Telemétrico Serializado em JSON ---")
    print(pacote_json)
    
    # Verificação da integridade sintática fazendo o parsing reverso
    try:
        dados_verificados = json.loads(pacote_json)
        print("\n[INFO]: Integridade sintática do JSON verificada com sucesso. Pronto para transmissão MQTT.")
    except json.JSONDecodeError as e:
        print(f"\n[ERRO]: Falha na integridade sintática do JSON: {e}")

# Execução da função
if __name__ == "__main__":
    serializar_dados_json()