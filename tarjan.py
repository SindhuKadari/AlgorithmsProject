from collections import defaultdict
class DirectedGraph:
    def __init__(self, N):
        self.N = N
        self.graph = defaultdict(list)
        self.index = 0
        self.stack = []
        self.on_stack = [False] * N
        self.indices = [-1] * N
        self.lowlink = [-1] * N
        self.SCCs = []
    def add_edge(self, u, v):
        self.graph[u].append(v)
    def _strongconnect(self, v):
        self.indices[v] = self.index
        self.lowlink[v] = self.index
        self.index += 1
        self.stack.append(v)
        self.on_stack[v] = True
        for w in self.graph[v]:
            if self.indices[w] == -1:
                self._strongconnect(w)
                self.lowlink[v] = min(self.lowlink[v], self.lowlink[w])
            elif self.on_stack[w]:
                self.lowlink[v] = min(self.lowlink[v], self.indices[w])
        # If v is a root node, pop the stack and generate an SCC
        if self.lowlink[v] == self.indices[v]:
            scc = []
            while True:
                w = self.stack.pop()
                self.on_stack[w] = False
                scc.append(w)
                if w == v:
                    break
            self.SCCs.append(scc)
    def tarjan_scc(self):
        for v in range(self.N):
            if self.indices[v] == -1:
                self._strongconnect(v)
        return self.SCCs
if __name__ == "__main__":
    graph = DirectedGraph(8)
    graph.add_edge(0, 1)
    graph.add_edge(1, 2)
    graph.add_edge(2, 3)
    graph.add_edge(3, 0)
    graph.add_edge(2, 4)
    graph.add_edge(4, 5)
    graph.add_edge(5, 6)
    graph.add_edge(6, 4)
    graph.add_edge(6, 7)
    sccs = graph.tarjan_scc()
    print("The Strongly Connected Components of the Graph (Tarjan's Algorithm):")
    for scc in sccs:
        print(scc)
