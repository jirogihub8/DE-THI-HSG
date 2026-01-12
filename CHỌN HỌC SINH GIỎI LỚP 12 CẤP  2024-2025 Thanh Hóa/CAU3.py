def check(x):
    dem=0
    for i in a:
        if i<x:
            dem+=x-i
            if dem>M:
                return False
    return True
f=open("CAU3.INP")
f1=open("CAU3.OUT","w")
N,M=map(int,f.readline().split())
a=list(map(int,f.readline().split()))
l=min(a)
r=l+M
re=l
while l<=r:
    m=(l+r)//2
    if check(m):
        re=m
        l=m+1
    else:
        r=m-1
f1.write(str(re))
f.close()
f1.close()
