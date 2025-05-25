from collections import defaultdict
class DirectedGraph:
    def __init__(self, N):
        self.N = N
        self.adj = defaultdict(list)
    def add_edge(self, a, d):
        self.adj[a].append(d)
    def _dfs(self, a, visited):
        visited[a] = True
        print(a, end=' ')
        for i in self.adj[a]:
            if not visited[i]:
                self._dfs(i, visited)
    def _fill_order(self, a, visited, stack):
        visited[a] = True
        for i in self.adj[a]:
            if not visited[i]:
                self._fill_order(i, visited, stack)
        stack.append(a)
    def _transpose(self):
        graph = DirectedGraph(self.N)
        for a in range(self.N):
            for i in self.adj[a]:
                graph.adj[i].append(a)
        return graph
    def print_strongly_connected_components(self):
        stack = []
        visited = [False] * self.N
        for i in range(self.N):
            if not visited[i]:
                self._fill_order(i, visited, stack)
        transposed_graph = self._transpose()
        visited = [False] * self.N
        while stack:
            a = stack.pop()
            if not visited[a]:
                transposed_graph._dfs(a, visited)
                print()
# Main execution
if __name__ == "__main__":
    graph = DirectedGraph(8)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(2, 4)
    graph.add_edge(3, 0)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(6, 7)
    print("The Strongly Connected Components of the Graph:")
    graph.print_strongly_connected_components()
