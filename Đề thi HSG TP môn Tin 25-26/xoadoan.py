n=int(input())
a=list(map(int,input().split()))
s=int(input())
if sum(a)<=s:
    print(0)
k=sum(a)-s
vt=[]
start=0
result=n+1
pre=[0]*(n+1)
for i in range(n):
    pre[i+1]=pre[i]+a[i]

else:
    print(pre)
    for j in range(n+1):
        
        while start<len(vt) and pre[j]-pre[vt[start]] >= k:
            l=j-vt[start]
            if l<result:
                result=l
            start += 1

        while start<len(vt) and pre[vt[-1]]>=pre[j]:
            vt.pop()

        vt.append(j)
    if result<=n:
        print(result)
    else:
        print(-1)
