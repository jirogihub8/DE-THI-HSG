f=open("cambay.inp")
f1=open("cambay.out","w")
n,m=map(int,f.readline().split())
cotmi=[]
hangmi=[]
cotma=[]
hangma=[]
ma=0
mi=int(3e11)
for i in range(n):
    a=list(map(int,f.readline().split()))
    for j in range(m):
        if a[j]>ma:
            ma=a[j]
            cotma=[j]
            hangma=[i]
            
        elif a[j]==ma:
            if j not in cotma:
                cotma.append(j)
            if i not in hangma:
                hangma.append(i)
        if a[j]<mi:
            mi=a[j]
            cotmi=[j]
            hangmi=[i]
            
        elif a[j]==mi:
            if j not in cotmi:
                cotmi.append(j)
            if i not in hangmi:
                hangmi.append(i)
N=set(hangma+hangmi)
M=set(cotma+cotmi)
print((n-len(N))*(m-len(M)))





