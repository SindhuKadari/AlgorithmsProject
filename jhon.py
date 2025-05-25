def dijkstra(v, cost, n):
    dist, visited = [float('inf')] * n, [False] * n
    dist[v] = 0
    for i in range(n): dist[i] = cost[v][i]
    dist[v] = 0
    for _ in range(n - 1):
        u = min((i for i in range(n) if not visited[i]), key=lambda x: dist[x], default=-1)
        if u == -1: break
        visited[u] = True
        for w in range(n):
            if not visited[w] and dist[u] + cost[u][w] < dist[w]:
                dist[w] = dist[u] + cost[u][w]
    return dist

def bellman_ford(v, edges):
    dist = [float('inf')] * v
    dist[-1] = 0
    for _ in range(v - 1):
        for u, w, cost in edges:
            if dist[u] + cost < dist[w]:
                dist[w] = dist[u] + cost
    for u, w, cost in edges:
        if dist[u] + cost < dist[w]:
            return dist, True
    return dist, False

def johnsons_algorithm(graph):
    nodes = list(graph)
    idx = {node: i for i, node in enumerate(nodes)}
    n = len(nodes)
    edges = [(idx[u], idx[v], graph[u][v]) for u in graph for v in graph[u]]
    for i in range(n): edges.append((n, i, 0))  # new vertex q

    h, neg_cycle = bellman_ford(n + 1, edges)
    if neg_cycle:
        print("Graph contains a negative-weight cycle.")
        return

    cost = [[float('inf')] * n for _ in range(n)]
    for u in graph:
        for v in graph[u]:
            i, j = idx[u], idx[v]
            cost[i][j] = graph[u][v] + h[i] - h[j]
        cost[idx[u]][idx[u]] = 0

    for i in range(n):
        dist = dijkstra(i, cost, n)
        print(f"\nFrom {nodes[i]}:")
        for j in range(n):
            d = dist[j]
            if d != float('inf'):
                print(f"To {nodes[j]}: {d - h[i] + h[j]}")
            else:
                print(f"To {nodes[j]}: Unreachable")

# Sample graph
graph = {
    'A': {'B': 10, 'F': 3},
    'B': {'C': 20},
    'C': {'E': 5, 'D': 15},
    'D': {'E': 12, 'G': 20},
    'E': {'G': 7},
    'F': {'G': 35},
    'G': {}
}

johnsons_algorithm(graph)
