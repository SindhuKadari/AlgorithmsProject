def kruskal(n, edges):
    parent = list(range(n))  # Initialize parent array for union-find
    # Find operation with path compression
    def find(u):
        while u != parent[u]:
            parent[u] = parent[parent[u]]  # Path compression
            u = parent[u]
        return u
    # Union operation to merge two sets
    def union(u, v):
        pu, pv = find(u), find(v)
        if pu == pv:
            return False  # Cycle detected
        parent[pu] = pv    # Union the sets
        return True
    # Sort edges by weight (greedy choice)
    edges.sort(key=lambda x: x[2])
    mst_weight = 0
    for u, v, w in edges:
        if union(u, v):  # Include edge if it doesn't form a cycle
            mst_weight += w
    return mst_weight
n = 5
edges = [
    (0, 1, 4), (0, 2, 6),
    (1, 2, 3), (1, 3, 8),
    (1, 4, 5), (2, 4, 7)
]
# Run Kruskal’s Algorithm
print("Kruskal’s MST Weight:", kruskal(n, edges))
