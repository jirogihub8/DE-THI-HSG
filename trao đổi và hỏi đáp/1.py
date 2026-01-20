import sys
f=sys.stdin
f1=f=sys.stdout
f=open("1.inp","r")
f1=open("all.out","w")

q=int(f.readline())
for _ in range(q):
    m,n,k=map(int,f.readline().split())
    maxr=min(m,k-1)
    ans=0
    if n+m<k:
        print(0)
    else:
        for r in range(maxr+1):
            maxtx=(m-r)//k+1
            need=(-r)%k
            if need<=n:
                maxty=(n-need)//k+1
            elif need>n:
                maxty=0
            ans+=(maxty*maxtx)
        print(ans)


