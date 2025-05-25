def minmax(arr):
  if len(arr)==1:
    return arr[0],arr[0]
  else:
    min=arr[0]
    max=arr[0]
    for i in range(len(arr)):
      if min<arr[i]:
        min=arr[i]
      if max>arr[i]:
        max=arr[i]
    return max,min
arr=[1,2,3,4,5,6,7,10,9]
print(minmax(arr))
