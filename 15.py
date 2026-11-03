# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 15

def processamento_vetorial_prodist():
    # Lista de tensões eficazes coletadas em barramento secundário[cite: 1]
    leituras_v = [220.0, 204.5, 218.0, 235.2, 222.1, 198.0, 228.4, 232.0, 208.5]
    v_base = 220.0
    
    # 1. Conversão para o sistema por unidade (pu) com arredondamento a 3 decimais utilizando list comprehension
    leituras_pu = [round(v / v_base, 3) for v in leituras_v]
    
    # 2. Filtragem de leituras transgressoras que violam a faixa adequada do PRODIST (V < 209.0 V ou V > 231.0 V)[cite: 1]
    transgressoes = [v for v in leituras_v if v < 209.0 or v > 231.0]
    
    # Exibição dos resultados formatados
    print(f"Lista em pu (3 decimais): {leituras_pu}")
    print(f"Lista de transgressões: {transgressoes}")

# Execução da função
if __name__ == "__main__":
    processamento_vetorial_prodist()