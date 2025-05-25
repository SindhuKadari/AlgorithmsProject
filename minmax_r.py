def minmax(arr):
  if len(arr)==1 :
    return arr[0],arr[0]
  elif len(arr)==2:
    return max(arr[0],arr[1]),min(arr[0],arr[1])
  else:
    mid=len(arr)//2
    max1,min1=minmax(arr[:mid])
    max2,min2=minmax(arr[mid:])
    return max(max1,max2),min(min1,min2)
arr=[1,2,3,4,5,6,7,8,9]
print(minmax(arr))
