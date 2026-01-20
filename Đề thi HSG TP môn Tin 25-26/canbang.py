n,k=map(int,input().split())
a=list(map(int,input().split()))
a=set(a)
d=0
for i in a:
    if i-k in a and i+k in a:
        d+=1
print(d)