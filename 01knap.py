def knapsack(n,p,m):
  x=[0]*n
  p.sort(key=lambda x:x[1])
  p=p[::-1]
  print(p)
  for i in range(n):
      if m>=p[i][1]:
        m=m-p[i][1]
        x[i]=1
      else:
        x[i]=0
  print("Solution vector",x)
  result=0
  for i in range(n):
    result+=x[i]*p[i][0]
  print("Optimal solution",result)
n=3
m=20
p=[[25,18],[24,15],[15,10]]
knapsack(n,p,m)
