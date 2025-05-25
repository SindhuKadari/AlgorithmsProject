def is_valid(v,pos,path,graph):
  if graph[path[pos-1]][v]==0:
    return False
  if v in path:
    return False
  return True
def ham_util(graph,path,pos):
  n=len(graph)
  if n==pos:
    return graph[path[pos - 1]][path[0]] == 1
  for i in range(1,n):
    if is_valid(i,pos,path,graph):
      path[pos]=i
      if ham_util(graph,path,pos+1):
        return True
      path[pos]=-1
  return False
def ham(graph):
  n=len(graph)
  path=[-1]*n
  path[0]=0
  if not ham_util(graph,path,1):
    print("Solution does not exist")
    return
  for i in range(n):
    print(path[i],end=" ")
  print(path[0])
graph = [[0, 1, 1, 1, 0,0],
    [1, 0, 1, 0, 1,0],
    [1, 1, 0, 1, 1,0],
    [1, 0, 1, 0, 1,1],
    [0, 1, 1, 1, 0,1],
    [0,0,0,1,1,0]]
ham(graph)
