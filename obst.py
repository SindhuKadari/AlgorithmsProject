def sum(f,i,j):
  s=0
  for k in range(i,j+1):
    s+=f[k]
  return s
def optcost(f,i,j):
  if j<i:
    return 0
  elif j==i:
    return f[i]
  else:
    freqsum=sum(f,i,j)
    min_val=float('inf')
    for r in range(i,j+1):
      cost=optcost(f,i,r-1)+optcost(f,r+1,j)
      min_val=min(min_val,cost)
    return min_val+freqsum
def obst(keys,f):
  n=len(keys)
  return optcost(f,0,n-1)
keys = [10, 12, 20]
freq = [34, 8, 50]
print(obst(keys,freq))
