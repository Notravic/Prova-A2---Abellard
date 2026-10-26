# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 7

def sistema_climatizacao_transformador(t_oleo: float):
    """
    Avalia a temperatura do topo do óleo (T_óleo) de um transformador de potência
    e aciona os estágios correspondentes de ventilação, alarme ou trip térmico.
    """
    if t_oleo < 65.0:
        print("VENTILACAO_NATURAL (ONAN)")
    elif 65.0 <= t_oleo < 80.0:
        print("VENTILACAO_FORCADA_ESTAGIO_1 (ONAF-1)")
    elif 80.0 <= t_oleo < 95.0:
        print("VENTILACAO_FORCADA_ESTAGIO_2 (ONAF-2) + ALARME")
    else:
        print("TRIP_TERMICO_EMERGENCIA - DESLASTRE TOTAL")

# Execução com o valor de entrada de teste especificado no enunciado[cite: 1]
if __name__ == "__main__":
    t_oleo_teste = 86.5  # Temperatura do topo do óleo em °C[cite: 1]
    sistema_climatizacao_transformador(t_oleo_teste)