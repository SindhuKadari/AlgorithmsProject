def topological_sort(graph):
    # Helper function to perform DFS and mark nodes
    def dfs(node):
        if node in temp_visited:
            return False  # If node is already in the current recursion stack, there's a cycle
        if node in visited:
            return True  # If node is already visited, no need to explore it
        temp_visited.add(node)  # Mark the node as being visited
        for neighbor in graph[node]:
            if not dfs(neighbor):
                return False  # If cycle is detected in the DFS of the neighbors, return False
        temp_visited.remove(node)  # Remove from the recursion stack after processing the node
        visited.add(node)  # Mark the node as fully processed
        top_order.append(node)  # Add the node to the topological order
        return True
    visited = set()  # To keep track of visited nodes
    temp_visited = set()  # To keep track of nodes in the current recursion stack (to detect cycles)
    top_order = []  # To store the topological order
    # Traverse each node in the graph
    for node in graph:
        if node not in visited:
            if not dfs(node):
                return "Graph has a cycle!"  # If a cycle is detected, return a message
    return top_order[::-1]  # Reverse the topological order to get correct result
# Example usage:
graph = {
    'A': ['B','C'],
    'B': ['E','G'],
    'C': ['F'],
    'D': ['B','C','G','F'],
    'E': [],
    'F': [],
    'G': ['E','F']
}
result = topological_sort(graph)
print(result)
