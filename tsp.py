def travelling_salesman(graph, s):
    n = len(graph)
    dp = [[float('inf')] * n for _ in range(1 << n)]
    dp[1 << s][s] = 0
    for mask in range(1 << n):
        for u in range(n):
            if (mask >> u) & 1:
                for v in range(n):
                    if not (mask >> v) & 1:
                        new_mask = mask | (1 << v)
                        dp[new_mask][v] = min(dp[new_mask][v], dp[mask][u] + graph[u][v])
    min_cost = float('inf')
    for i in range(n):
        if i != s:
            min_cost = min(min_cost, dp[(1 << n) - 1][i] + graph[i][s])
    return min_cost
graph = [[0, 10, 15, 20],
         [5, 0, 9, 10],
         [6, 13, 0, 12],
         [8, 8, 9, 0]]
print("The minimum cost of visiting all nodes is:", travelling_salesman(graph, 0))
