def job(n,p):
  if n==0:
    return 0
  elif n==1:
    return p[0][0]
  else:
    p.sort(key=lambda x:x[0])
    p=p[::-1]
    max_t=max(p,key=lambda x:x[1])[1]
    r=[None]*max_t
    for i in range(n):
      t=p[i][1]
      while t>0:
        if r[t-1] is None:
          r[t-1]=p[i]
          break
        else:
          t=t-1
    return r
n=9
p=[[15,7],[20,2],[30,5],[18,3],[18,4],[10,5],[23,2],[16,7],[25,3]]
a=job(n,p)
print("Solution vector",a)
sum=0
for i in range(len(a)):
    sum+=a[i][0]
print("Optimal Solution ",sum)
