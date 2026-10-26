# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 5

def validar_sinal_telemetria(v: float, i: float, f: float):
    """
    Função para validação e filtragem física de sinais de telemetria.
    Verifica se a tensão, a corrente e a frequência estão dentro dos limites operacionais.
    """
    # Verificação das condições físicas regulamentadas
    if v >= 0.0 and i >= 0.0 and (45.0 <= f <= 65.0):
        print("TELEMETRIA_VALIDA")
    else:
        print("FALHA_SINAL: Transdutor corrompido")

# Execução com os casos de teste especificados no enunciado
if __name__ == "__main__":
    print("--- Caso de Teste 1 ---")
    validar_sinal_telemetria(v=220.0, i=-5.0, f=60.0)
    
    print("\n--- Caso de Teste 2 ---")
    validar_sinal_telemetria(v=13800.0, i=48.2, f=59.95)