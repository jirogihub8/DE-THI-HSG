def uoc(x):
    c=set()
    c.add(1)
    for i in x:
        c.add(i)
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                c.add(j)
                if i//j!=i:
                    c.add(i//j)
    return c
f=open("CAU4.INP")
f1=open("CAU4.OUT","w")
N,K=map(int,f.readline().split())
a=list(map(int,f.readline().split()))
l_uoc=uoc(a)
mod=10**9+7
dp=[0]*(N+1)
dp[1]=1
for i in range(2,N+1):
    t=0
    for j in l_uoc:
        if j<=i-1: # vì nó đi từ 1
            t+=dp[i-j]
            t%=mod
        else:
            break    
    dp[i]=t
f1.write(str(dp[N]))
f.close()
f1.close()