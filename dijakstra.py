def dijkstra(v, cost, n):
    dist = [float('inf')] * n
    s = [False] * n
    dist[v] = 0
    s[v] = True
    for i in range(n):
        dist[i] = cost[v][i]
    dist[v] = 0
    for _ in range(n - 1):
        min_dist = float('inf')
        u = -1
        for j in range(n):
            if not s[j] and dist[j] < min_dist:
                min_dist = dist[j]
                u = j
        if u == -1:
            break
        s[u] = True
        for w in range(n):
            if not s[w] and dist[u] + cost[u][w] < dist[w]:
                dist[w] = dist[u] + cost[u][w]
    return dist
graph = {
    'A': {'B': 10, 'F': 3},
    'B': {'C': 20},
    'C': {'E': 5, 'D': 15},
    'D': {'E': 12, 'G': 20},
    'E': {'G': 7},
    'F': {'G': 35},
    'G': {}
}
nodes = list(graph.keys())
n = len(nodes)
cost_matrix = [[float('inf')] * n for _ in range(n)]

for i, from_node in enumerate(nodes):
    for j, to_node in enumerate(nodes):
        if to_node in graph[from_node]:
            cost_matrix[i][j] = graph[from_node][to_node]
        if from_node == to_node:
            cost_matrix[i][j] = 0
start_node = input("Enter the starting node: ")
if start_node not in nodes:
    print("Invalid starting node. Please enter a valid node from the graph.")
else:
    start_index = nodes.index(start_node)
    shortest_distances = dijkstra(start_index, cost_matrix, n)
    print("\nShortest distances from node", start_node)
    for i, distance in enumerate(shortest_distances):
        print(f"{nodes[i]}: {distance}")
