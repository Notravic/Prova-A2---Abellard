# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 8

def classificar_qualidade_energia_prodist(v_media: float):
    """
    Classifica a tensão eficaz média de um alimentador de acordo com o Módulo 8 do PRODIST
    e indica se a concessionária está sujeita a compensação financeira.
    """
    # Verificação de Tensão Adequada
    if 202.0 <= v_media <= 231.0:
        status = "TENSAO_ADEQUADA"
        acao = "Dentro dos limites regulatorios. Sem penalizacoes."
        
    # Verificação de Tensão Precária
    elif (191.0 <= v_media < 202.0) or (231.0 < v_media <= 233.0):
        status = "TENSAO_PRECARIA"
        acao = "Sujeito a penalizacao e compensacao financeira"
        
    # Caso contrário, enquadra-se como Tensão Crítica
    else:
        status = "TENSAO_CRITICA"
        acao = "Sujeito a penalizacao e compensacao financeira"
        
    print(f"Status: {status} | Acao: {acao}")

# Execução com o valor de entrada de teste especificado no enunciado[cite: 1]
if __name__ == "__main__":
    tensao_media = 188.4  # Tensão eficaz média em Volts[cite: 1]
    classificar_qualidade_energia_prodist(tensao_media)