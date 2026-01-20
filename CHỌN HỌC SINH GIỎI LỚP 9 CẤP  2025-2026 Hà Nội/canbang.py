f=open("canbang.inp")
f1=open("canbang.out","w")
n,k=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
a=set(list(a))
d=0
for i in a:
    if i-k in a and i+k in a:
        d+=1
f1.write(str(d))
f.close()
f1.close()