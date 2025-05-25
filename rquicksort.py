import random
def quicksort(a,l,h):
  if l>=h:
    return
  pi=random.randint(l,h)
  pv=a[pi]
  a[pi],a[h]=a[h],a[pi]
  i=l
  for j in range(l,h):
    if a[j]<=pv:
      a[i],a[j]=a[j],a[i]
      i+=1
  a[i],a[h]=a[h],a[i]
  quicksort(a,l,i-1)
  quicksort(a,i+1,h)
a=[1,12,3,0,9,1]
quicksort(a,0,len(a)-1)
print(a)
