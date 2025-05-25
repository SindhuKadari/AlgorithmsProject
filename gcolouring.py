def graph_coloring(graph, k):
    num_vertices = len(graph)
    vertices = list(graph.keys())
    color = {v: 0 for v in vertices}
    def is_safe(vertex, c):
        for neighbor in graph.get(vertex, []):
            if color[neighbor] == c:
                return False
        return True
    def graph_coloring_util(vertex_index):
        if vertex_index == num_vertices:
            return True
        vertex = vertices[vertex_index]
        for color_index in range(1, k + 1):
            if is_safe(vertex, color_index):
                color[vertex] = color_index
                if graph_coloring_util(vertex_index + 1):
                    return True
                color[vertex] = 0
        return False
    if graph_coloring_util(0):
        print(f"Graph can be colored with {k} colors.")
        print("Color assignment:")
        for v, c in color.items():
            print(f"Vertex {v}: Color {c}")
        return color
    else:
        print(f"Graph cannot be colored with {k} colors.")
        return None
adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]]
graph_dict = {i: [j for j, connected in enumerate(row) if connected] for i, row in enumerate(adjacency_matrix)}
k1 = 2
coloring1 = graph_coloring(graph_dict, k1)
print("-" * 20)
