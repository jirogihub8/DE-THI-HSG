f=open("2.inp")
n,m=map(int,f.readline().split())
d=[]
for i in range(n):
    a,b=map(int,f.readline().split())
    tb=a//b
    d.append(tb)
d.sort()
