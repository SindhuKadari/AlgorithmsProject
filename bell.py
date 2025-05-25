def bellman_ford(num_vertices, edges, source):
    INF = float('inf')
    dist = [INF] * num_vertices
    dist[source] = 0
    for _ in range(num_vertices - 1):
        for u, v, w in edges:
            if dist[u] != INF and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
    has_negative_cycle = False
    for u, v, w in edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            has_negative_cycle = True
            break
    return dist, has_negative_cycle
if __name__ == "__main__":
    edges_list = [
        (0, 1, 2),
        (0, 5, 3),
        (0, 3, 5),
        (1, 4, 1),
        (2, 6, 4),
        (2, 1, 7),
        (3, 4, 3),
        (4, 2, -3),
        (4, 6, 3),
        (5, 1, -4),
        (6, 3, -1)
    ]
    num_vertices = max(max(u, v) for u, v, w in edges_list) + 1
    distances, has_cycle = bellman_ford(num_vertices=num_vertices, edges=edges_list, source=0)
    if has_cycle:
        print("A negative-weight cycle is reachable from the source.")
    else:
        print("Shortest distances from source 0:")
        for i, d in enumerate(distances):
            print(f"Distance to vertex {i}: {d}")
