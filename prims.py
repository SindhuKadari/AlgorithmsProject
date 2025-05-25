import heapq  # Import heapq for priority queue
def prim(n, graph, start=0):
    visited = [False] * n          # Track visited vertices
    min_heap = [(0, start)]        # Start with (weight=0, start vertex)
    mst_weight = 0                 # Store total weight of the MST
    while min_heap:
        cost, u = heapq.heappop(min_heap)  # Choose the edge with minimum weight
        if visited[u]:
            continue
        visited[u] = True          # Mark current vertex as visited
        mst_weight += cost         # Add edge's weight to MST total
        # Add all edges from u to unvisited neighbors
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))
    return mst_weight  # Return total weight of the MST
n = 5  # Number of vertices
# Adjacency list of an undirected weighted graph
graph = {
    0: [(1, 2), (3, 6)],
    1: [(0, 2), (2, 3), (3, 8), (4, 5)],
    2: [(1, 3), (4, 7)],
    3: [(0, 6), (1, 8)],
    4: [(1, 5), (2, 7)]
}
# Run Prim’s algorithm and print MST weight
print("Prim’s MST Weight:", prim(n, graph))
