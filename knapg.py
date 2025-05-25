def knapsack(n,m,p,w):
    wr=[]
    x=[0]*n
    for i in range(n):
        wr.append(p[i]/w[i])
    while m>0:
        for i in range(n):
            if wr[i]==max(wr):
                Max=i
                wr[Max]=0
                break
        if w[Max]<=m:
            m=m-w[Max]
            x[Max]=1
        else:
            temp=m/w[Max]
            m=0
            x[Max]=temp
    print("Solution vector:",x)
    result=0
    for i in range(n):
        result+=x[i]*p[i]
    print("Optimal solution",result)
n=4
m=10
p=[24,18,18,10]
w=[5,4,3,2]
knapsack(n,m,p,w)
