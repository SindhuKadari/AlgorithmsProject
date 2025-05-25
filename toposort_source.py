from collections import deque
def topological_sort(graph):
    # Step 1: Calculate in-degree (number of incoming edges) for each node
    in_degree = {node: 0 for node in graph}  # Initialize in-degree to 0 for all nodes
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1
    # Step 2: Collect all nodes with no incoming edges (in-degree 0)
    queue = deque([node for node in graph if in_degree[node] == 0])
    top_order = []  # To store the topological order
    while queue:
        node = queue.popleft()
        top_order.append(node)
        # Step 3: Reduce in-degree of neighbors
        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    # If top_order doesn't contain all nodes, the graph has a cycle
    if len(top_order) == len(graph):
        return top_order
    else:
         return "Graph has a cycle!"
# Example usage:
graph = {
    'A': ['C','B', 'D'],
    'B':['E'],
    'C':['E','F','G'],
    'D':['C','F'],
    'E':['G'],
    'F':['G'],
    'G':[]
    }
result = topological_sort(graph)
print(result)
