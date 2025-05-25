def fib_r(k):
  if k==0:
    return 0
  elif k==1:
    return 1
  else:
    return fib_r(k-1)+fib_r(k-2)
n=10
print("Recursive Fibonacci:", [fib_r(i) for i in range(n)])
def fib_i(n):
  if n==0:
    return 0
  elif n==1:
    return 1
  else:
    a,b=0,1
    for i in range(2,n+1):
      a,b=b,a+b
    return b
n=10
print("Iterative Fibonacci:", [fib_i(i) for i in range(n)])

