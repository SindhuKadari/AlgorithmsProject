#(18) BICONNECTED
class Graph:
    def __init__(self, n):
        self.n = n
        self.adj = [[] for _ in range(n)]

    def addEdge(self, u, v):
        self.adj[u].append(v)
        self.adj[v].append(u)

def biconnected_components_and_articulation_points(graph):
    n = graph.n
    disc = [-1] * n
    low = [-1] * n
    stack = []
    bcc_list = []
    articulation_points = set()
    time_counter = [0]

    def dfs(u, parent):
        disc[u] = time_counter[0]
        low[u] = time_counter[0]
        time_counter[0] += 1
        children_count = 0

        for v in graph.adj[u]:
            if v == parent:
                continue
            if disc[v] == -1:
                children_count += 1
                stack.append((u, v))
                dfs(v, u)
                low[u] = min(low[u], low[v])

                # Articulation point logic
                if parent != -1 and low[v] >= disc[u]:
                    articulation_points.add(u)

                # Biconnected component logic
                if low[v] >= disc[u]:
                    bcc = []
                    while stack and stack[-1] != (u, v):
                        bcc.append(stack.pop())
                    bcc.append(stack.pop())
                    bcc_list.append(bcc)
            elif disc[v] < disc[u]:
                low[u] = min(low[u], disc[v])
                stack.append((u, v))

        # Root of DFS tree is an articulation point if it has two or more children
        if parent == -1 and children_count > 1:
            articulation_points.add(u)
    # Perform DFS for all vertices
    for i in range(n):
        if disc[i] == -1:
            dfs(i, -1)
            # Add remaining edges in the stack as a component
            if stack:
                bcc = []
                while stack:
                    bcc.append(stack.pop())
                bcc_list.append(bcc)

    return bcc_list, articulation_points
if __name__ == "__main__":
    g1 = Graph(7)
    g1.addEdge(1, 4)
    g1.addEdge(1, 2)
    g1.addEdge(4, 3)
    g1.addEdge(2, 3)
    g1.addEdge(3, 5)
    g1.addEdge(3, 6)
    bccs, art_points = biconnected_components_and_articulation_points(g1)
    print("Biconnected Components (each as a list of edges):")
    for idx, comp in enumerate(bccs, start=1):
        print(f"Component {idx}: {comp}")
    print("\nArticulation Points:")
    for point in art_points:
        print(f"Vertex {point}")
