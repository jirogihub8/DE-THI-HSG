f=open("SOKHONG.INP")
f1=open("SOKHONG.OUT","w")
n,k,r=map(int,f.readline().split())
a=[0]+list(map(int,f.read().split()))
t=[5,25,125]
l=[0]
for i in range(1,501):
    s=0
    for j in range(3):
        s+=i//t[j]
    l.append(s)
result=0
for i in range(k,r+1):
    result+=l[a[i]]
f1.write(str(result))
f.close()
f1.close()