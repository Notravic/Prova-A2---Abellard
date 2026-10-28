# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 17

def modelagem_semantica_alimentador():
    # Criação do dicionário com os atributos do alimentador[cite: 1]
    alimentador = {
        "tag": "AL-01",
        "subestacao": "SE-CENTRAL",
        "tensao_kv": 13.8,
        "corrente_a": 142.5,
        "disjuntor_fechado": True
    }
    
    print("--- Consulta Segura com .get() ---")
    # Utiliza o método .get() para buscar com segurança a chave "temperatura_oleo_c", atribuindo 25.0 °C como padrão[cite: 1]
    temp_oleo = alimentador.get("temperatura_oleo_c", 25.0)
    print(f"Temperatura do óleo (valor padrão): {temp_oleo} °C (Consulta executada sem KeyError)")
    
    print("\n--- Atualização com .update() ---")
    # Utiliza o método .update() para registrar a temperatura real de 78.2 °C e o alarme "ALERTA_TERMICO"[cite: 1]
    alimentador.update({
        "temperatura_oleo_c": 78.2,
        "alarme": "ALERTA_TERMICO"
    })
    
    # Imprime o dicionário atualizado iterando sobre .items()[cite: 1]
    print("Atributos atualizados do alimentador:")
    for chave, valor in alimentador.items():
        print(f"  {chave}: {valor}")

# Execução da função
if __name__ == "__main__":
    modelagem_semantica_alimentador()