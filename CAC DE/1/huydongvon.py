
from collections import Counter
f=open("HUYDONGVON.INP")
f1=open("HUYDONGVON.OUT","w")
n,S=list(map(int,f.readline().split()))
a=list(map(int,f.readline().split()))
m=sorted(set(a))
s=Counter(a)
lm=len(m)
l=[0]*(lm)
if sum(a)<S:
    f.write(str('-1'))
else:
    i=0
    
    while sum(l)<S:
        l[i:]=[m[i]]*(lm-i)
        i+=1
    if sum(l)>S:
        i-=1
        need=S-sum(l[:i])
        now=l[i:]
        
        
        
f.close()
f1.close()
        
        
f.close()
f1.close()