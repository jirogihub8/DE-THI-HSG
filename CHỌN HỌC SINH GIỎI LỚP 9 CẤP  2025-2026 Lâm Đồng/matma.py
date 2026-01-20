f=open("matma.inp")
f1=open("matma.out","w")
a,n=map(int,f.readline().split())
d={}
so_cuoi=a%10
if so_cuoi==1 or so_cuoi==0:
    print(so_cuoi)
else:
    for i in range(2,10):
        if i not in d:
            d[i]=[]
        for j in range(1,6):
            t=(i**j)%10
            if t not in d[i]:
                d[i].append(t)
    print(d)
    T=d[so_cuoi]
    t=n%len(T)
    if t==0:
        t=len(T)
    print(d[so_cuoi][t-1])