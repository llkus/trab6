import networkx as nx
import matplotlib.pyplot as plt

def dijkstra(matriz, inicio):
    num_vertices = len(matriz)
    distancias = [float('inf')] * num_vertices
    distancias[inicio] = 0
    visitados = set()
    fila = [(0, inicio)]

    while fila:
        custo, no_atual = min(fila)
        fila.remove((custo, no_atual))
        if no_atual in visitados:
            continue
        visitados.add(no_atual)

        for vizinho in range(num_vertices):
            if matriz[no_atual][vizinho] > 0:
                novo_custo = distancias[no_atual] + matriz[no_atual][vizinho]
                if novo_custo < distancias[vizinho]:
                    distancias[vizinho] = novo_custo
                    fila.append((novo_custo, vizinho))

    return distancias


matriz_adjacencia = [
    [0, 5, 7, 1, 0, 0, 0],
    [0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 6, 5, 0, 0],
    [0, 3, 0, 0, 0, 5, 3],
    [0, 0, 0, 0, 0, 4, 0],
    [0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0]
]


vertice_inicio = int(input("Digite o vértice de origem (1 a 7): ")) - 1


distancias = dijkstra(matriz_adjacencia, vertice_inicio)


arvore = nx.Graph()


for i in range(len(matriz_adjacencia)):
    for j in range(len(matriz_adjacencia[i])):
        if matriz_adjacencia[i][j] > 0:
            arvore.add_edge(i+1, j+1, weight=matriz_adjacencia[i][j])


minima_arvore = nx.minimum_spanning_tree(arvore)


pos = nx.spring_layout(minima_arvore)
nx.draw_networkx(minima_arvore, pos, with_labels=True, node_color='lightblue', node_size=500, edge_color='gray', width=2)
labels = nx.get_edge_attributes(minima_arvore, 'weight')
nx.draw_networkx_edge_labels(minima_arvore, pos, edge_labels=labels)
plt.axis('off')
plt.show()


print("Distâncias mínimas a partir do vértice", vertice_inicio+1)
for i in range(len(distancias)):
    if i != vertice_inicio:
        print(f"Vértice {i+1}: Distância = {distancias[i]}")
