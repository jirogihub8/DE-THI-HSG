f=open("GIAIDB.INP")
f1=open("GIAIDB.OUT","w")
n,k=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
b=list(map(int,f.readline().split()))
m=999999999
d=1
for i in range(n):
    if a[i]>=k:
        if b[i]<m:
            m=b[i]
            d=1
        elif b[i]==m:
            d+=1
            print(d)
f1.write(str(d)+' '+str(m))
f.close()
f1.close()
