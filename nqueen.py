def is_safe(n,board,row,col):
  for i in range(row):
    if board[i]==col  or  board[i]-i==col-row or board[i]+i==col+row:
      return False
  return True
def n_queen(n,board,row):
  if row==n:
    return [board[:]]
  else:
    solutions=[]
    for col in range(n):
      if is_safe(n,board,row,col):
        board[row]=col
        solutions.extend(n_queen(n,board,row+1))
    return solutions
def solve(n):
  board=[-1]*n
  return n_queen(n,board,0)
n=4
solutions=solve(n)
# Print each solution
for solution in solutions:
    for row in solution:
        print("".join(['q' if row == col else '-' for col in range(n)]))
    print()
