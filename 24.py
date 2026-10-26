# Nomes: Rafael Leme Soares - RGM 46677062 / Mateus Henrique Espósito Lima - RGM 46678883 / Pedro Lucas Alves Faustino - RGM 46636480 / Alysson Silva de Andrade - RGM 46699929 / Danilo Correa da Silva - RGM 46606718
# Disciplina: Inteligência Artificial e Programação Para Engenharia
# Prova A2 - Exercício: 24

import numpy as np

def solucao_fluxo_carga_linear():
    # Parâmetros do sistema de 3 barras
    n_barras = 3
    
    # Lista de conexões no formato (barra_de, barra_para, Z_serie)
    linhas = [
        (1, 2, 0.20 + 0.40j),
        (2, 3, 0.10 + 0.20j),
        (1, 3, 0.20 + 0.40j)
    ]
    
    # Construção da Matriz Y_bus completa (3 x 3)
    y_bus = np.zeros((n_barras, n_barras), dtype=complex)
    for de, para, z_serie in linhas:
        k = de - 1
        m = para - 1
        y_serie = 1.0 / z_serie
        y_bus[k, m] -= y_serie
        y_bus[m, k] -= y_serie
        y_bus[k, k] += y_serie
        y_bus[m, m] += y_serie
        
    print("--- Matriz Y_bus (Siemens) ---")
    print(np.round(y_bus, 4))
    
    # Vetor de injeções de corrente nodais conhecidas [ I ]
    i_nodal = np.array([
        50.0 + 0.0j,
        -25.0 - 10.0j,
        -25.0 + 10.0j
    ], dtype=complex)
    
    # Para evitar matriz singular (Barra de folga/referência na Barra 1 com V1 fixa),
    # isolamos as barras de carga (Barra 2 e Barra 3) eliminando a dependência linear:
    # Definimos a tensão fixa da Barra 1 (ex: 220 V ou 1.0 pu)
    v_1 = 220.0 + 0.0j
    
    # Submatrizes para o sistema reduzido das barras 2 e 3 (índices 1 e 2)
    # I_livre = Y_22 * V_livre + Y_21 * V_1  ==>  Y_22 * V_livre = I_livre - Y_21 * V_1
    y_livre = y_bus[1:, 1:]
    i_livre = i_nodal[1:]
    y_col_1 = y_bus[1:, 0:1]
    
    i_modificado = i_livre - (y_col_1 * v_1).flatten()
    
    # Resolução do sistema linear não singular para as tensões desconhecidas (Barras 2 e 3)
    v_livre = np.linalg.solve(y_livre, i_modificado)
    
    # Montagem do vetor completo de tensões nodais
    v_nodal = np.insert(v_livre, 0, v_1)
    
    # Extração das magnitudes das tensões nodais
    magnitudes_tensao = np.abs(v_nodal)
    
    print("\n--- Resultados da Solução Linear (Com Barra de Referência) ---")
    for idx, v_mag in enumerate(magnitudes_tensao, start=1):
        print(f"Barra {idx} -> Tensão Nodal (Magnitude): {v_mag:.4f} V")

# Execução da função
if __name__ == "__main__":
    solucao_fluxo_carga_linear()