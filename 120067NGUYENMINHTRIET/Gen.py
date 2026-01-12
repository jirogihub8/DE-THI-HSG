def sanguoc(x):
    T=[1]*(x+3)
    for i in range(2,int(x**0.5)+1):
        for j in range(i*i,x+1,i):
            T[j]+=i
            if i*i!=j:
                T[j]+=j//i
    return T


f=open("GEN.INP")
f1=open("GEN.OUT","w")
n=int(f.readline())
a=list(map(int,f.readline().split()))
dem=0
g=sanguoc(max(a))
for i in a:
    if g[i]<i:
        dem+=1
f1.write(str(dem))
f.close()
f1.close()
