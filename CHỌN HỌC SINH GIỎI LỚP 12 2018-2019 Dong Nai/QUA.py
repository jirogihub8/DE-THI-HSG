f=open("QUA.INP")
f1=open("QUA.OUT","w")
m,n,k=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
b=list(map(int,f.readline().split()))
a.sort()
b.sort()
banh=0
keo=n-1
dem=0
while keo>=0 and banh<=m-1:
    if a[banh]+b[keo]<=k:
        dem+=1
        banh+=1
        keo-=1
    elif a[banh]+b[keo]>k:
        keo-=1
print(dem)
f.close()
f1.close()