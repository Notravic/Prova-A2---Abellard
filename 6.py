# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 6

def reles_sobrecorrente(i_nom: float, i_medida: float):
    """
    Simula a atuação de um relé digital de proteção de sobrecorrente (ANSI 50 / ANSI 51).
    Avalia a corrente medida pelo Transformador de Corrente (TC) face à corrente nominal.
    """
    if i_medida <= i_nom:
        print("REGIME_NORMAL")
    elif i_nom < i_medida <= 2.5 * i_nom:
        print("SOBRECARGA_TEMPORIZADA (ANSI 51)")
    else:
        print("TRIP_INSTANTANEO (ANSI 50) - DISJUNTOR ABERTO")

# Execução com os valores de entrada de teste especificados no enunciado[cite: 1]
if __name__ == "__main__":
    i_nom = 100.0   # Corrente nominal da instalação em Amperes[cite: 1]
    i_medida = 265.0 # Corrente medida pelo TC em Amperes[cite: 1]
    
    reles_sobrecorrente(i_nom, i_medida)