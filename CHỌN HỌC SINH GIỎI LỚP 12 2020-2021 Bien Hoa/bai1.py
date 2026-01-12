def sangnt(x):
    c=[True]*(x+3)
    for i in range(2,int(x**0.5)+1):
        if c[i]:
            for j in range(i*i,x+1,i):
                c[j]=False
    l=[]
    for i in range(2,x+1):
        if c[i]==True:
            l.append(i)
    return l
g=sangnt(100000)
def thuasont(x):
    i=0
    ans=[]
    while x!=1 and i<len(g):
        if x%g[i]==0:
            ans+=[g[i]]
            while x%g[i]==0:
                x//=g[i]
        else:
            i+=1
    if x>1:
        ans+=[x]
    return ans
f=open("bai1.inp")
f1=open("bai1.out","w")
a,b=map(int,f.readline().split())
C=set(thuasont(a)+thuasont(b))
f1.write(str(len(C)))
f.close()
f1.close()