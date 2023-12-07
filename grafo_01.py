from utils import end_time_fun, start_time_fun


def calcular_distancia(permutacao, matriz_distancias):
    distancia = 0
    for i in range(len(permutacao) - 1):
        cidade_atual = permutacao[i]
        proxima_cidade = permutacao[i + 1]

        if matriz_distancias[cidade_atual][proxima_cidade] == float("inf"):
            # Ignorando a rotas, pois não existe um caminho por está rota
            return float("inf")

        distancia += matriz_distancias[cidade_atual][proxima_cidade]

    distancia += matriz_distancias[permutacao[-1]][permutacao[0]]
    return distancia


def gerar_permutacoes(cidades):
    if len(cidades) == 0:
        return [[]]

    permutacoes = []
    for i in range(len(cidades)):
        cidade_atual = cidades[i]
        restante = cidades[:i] + cidades[i + 1 :]
        subpermutacoes = gerar_permutacoes(restante)
        for permutacao in subpermutacoes:
            permutacoes.append([cidade_atual] + permutacao)
    return permutacoes


def caixeiro_viajante_forca_bruta(matriz_distancias):
    num_cidades = len(matriz_distancias)
    cidades = list(range(num_cidades))
    melhores_permutacoes = []
    menor_distancia = float("inf")

    permutacoes = gerar_permutacoes(cidades)

    for permutacao in permutacoes:
        distancia_atual = calcular_distancia(permutacao, matriz_distancias)
        if distancia_atual < menor_distancia:
            menor_distancia = distancia_atual
            melhores_permutacoes = permutacao

    return melhores_permutacoes, menor_distancia


def imprimir_matriz_com_menor_caminho(matriz_distancias: list[list[int | float]]):
    melhores_caminhos, menor_distancia = caixeiro_viajante_forca_bruta(
        matriz_distancias
    )

    indices_menor_caminho = []

    # print(melhores_caminhos)
    for i in range(len(melhores_caminhos) - 1):
        indices_menor_caminho.append((melhores_caminhos[i], melhores_caminhos[i + 1]))

    indices_menor_caminho.append((melhores_caminhos[-1], melhores_caminhos[0]))

    print("Matriz de Distâncias:")

    for i, linha in enumerate(matriz_distancias):
        for j, distancia in enumerate(linha):
            if (i, j) in indices_menor_caminho:
                print(f" X{i+1}  \t", end="")
            else:
                print(f"{distancia}\t", end="")
        print()

    print("\nMelhor Caminho:", end=" ")

    for cidade in melhores_caminhos:
        print(f"Cidade {cidade} -> ", end="")

    print(f"Cidade {melhores_caminhos[0]}")

    print("Menor Distância:", menor_distancia)


# float("inf") representa que a ligação entre as duas vértices não existe
matriz_distancias: list[list[int | float]] = [
    [0, 2, float("inf"), 3, 6],
    [2, 0, 4, 3, float("inf")],
    [float("inf"), 4, 0, 7, 3],
    [3, 3, 7, 0, 3],
    [6, float("inf"), 3, 3, 0],
]

start_time = start_time_fun()
imprimir_matriz_com_menor_caminho(matriz_distancias)
print("--- %s seconds ---" % (end_time_fun(start_time)))

# OUTPUT
# Melhor Caminho: Cidade 0 -> Cidade 1 -> Cidade 2 -> Cidade 4 -> Cidade 3 -> Cidade 0
# Menor Distância: 15
# --- 0.0004673004150390625 seconds ---
