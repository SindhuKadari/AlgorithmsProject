def matrix_chain_order(p):
    n = len(p) - 1
    m = [[0] * n for _ in range(n)]  # Initialize m with zeros
    s = [[0] * n for _ in range(n)]  # Initialize s with zeros
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            m[i][j] = float('inf')
            for k in range(i, j):
                q = m[i][k] + m[k + 1][j] + p[i] * p[k + 1] * p[j + 1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m, s
def print_optimal_parens(s, i, j):
    if i == j:
        print(f'A{i + 1}', end='')
    else:
        print('(', end='')
        print_optimal_parens(s, i, s[i][j])
        print_optimal_parens(s, s[i][j] + 1, j)
        print(')', end='')
p = [5, 4, 6, 2, 7]
m, s = matrix_chain_order(p)
for row in m:
    print(row)
for i in s:
    print(i)
print('\nOptimal Parenthesization: ')
print_optimal_parens(s, 0, len(p) - 2)
