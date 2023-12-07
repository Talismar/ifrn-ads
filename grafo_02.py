from itertools import permutations

from numpy import isnan, where
from pandas import read_excel

from utils import end_time_fun, start_time_fun

# Lendo o excel com os dados de pesos entre as cidades
excel = read_excel("grafo.ods", engine="odf")
data_numpy = where(isnan(excel.to_numpy()), 99999, excel.to_numpy())

matriz_adjancente: list[list[int]] = []

for row_index, row_data in enumerate(data_numpy.tolist()):
    matriz_adjancente.append([])
    for item in row_data:
        matriz_adjancente[row_index].append(int(item) if item != 99999 else item)


def calcular_distancia(permutacao, matriz_adjacente):
    distancia = 0
    for i in range(len(permutacao) - 1):
        cidade_atual = permutacao[i]
        proxima_cidade = permutacao[i + 1]

        if matriz_adjacente[cidade_atual][proxima_cidade] == 99999:
            return 99999

        distancia += matriz_adjacente[cidade_atual][proxima_cidade]

    distancia += matriz_adjacente[permutacao[-1]][permutacao[0]]
    return distancia


def gerar_permutacao_valida(matriz_distancias):
    cidades_valid: list[list[int]] = []

    for row_index, row in enumerate(matriz_distancias):
        cidades_valid.append([])
        for value in row:
            if value != 99999:
                cidades_valid[row_index].append(value)

    permutations_cidades_validas = []
    for index, cidades in enumerate(cidades_valid):
        permutations_cidades_validas.append(permutations(cidades))

    return permutations_cidades_validas


quant_cidades = len(matriz_adjancente)
cidades = list(range(quant_cidades))
ponto_partida = 0
melhores_permutacoes: tuple[int, ...] | None = None
menor_distancia = 99999

permutacoes = permutations([cidade for cidade in cidades if cidade != ponto_partida])

start_time = start_time_fun()

for permutacao in permutacoes:
    distancia_atual = calcular_distancia(
        tuple([ponto_partida] + list(permutacao)), matriz_adjancente
    )
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        melhores_permutacoes = permutacao

print(melhores_permutacoes, menor_distancia)
print("--- %s seconds ---" % (end_time_fun(start_time)))

# OUTPUT
# Não conseguir encontrar o caminho ainda na minha máquina, porque demorou muito
