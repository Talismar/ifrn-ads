from binary_tree import BinarySearchTree


sequences = [[1, 2, 3, 4, 5, 6, 7, 8, 9], [3, 2, 6, 5, 4, 1, 7, 8, 9]]

for index, sequence in enumerate(sequences):
    binary_tree_instance = BinarySearchTree()

    # 1 - Faça um algoritmo para preencher as seguintes sequências:  [1 2 3 4 5 6 7 8 9] e [3 2 6 5 4 1 7 8 9], respectivamente  # noqa: E501
    for i in sequence:
        binary_tree_instance.insert(i)

    # 2 - Escreva um algoritmo para encontrar o maior e o menor número de uma árvore binária # noqa: E501
    print("Minor >> ", binary_tree_instance.find_minor())
    print("Greater >> ", binary_tree_instance.find_greater())

    # 3 - Escreva um algoritmo para encontrar um número em uma árvore binária
    print(binary_tree_instance.search(8))

    # 4 - Escrever um algoritmo que retorne quantos nós folhas existem na árvore
    print(binary_tree_instance.count_nodes(binary_tree_instance.root))
    print(binary_tree_instance)

    if index < len(sequences) - 1:
        print("-" * 50)
