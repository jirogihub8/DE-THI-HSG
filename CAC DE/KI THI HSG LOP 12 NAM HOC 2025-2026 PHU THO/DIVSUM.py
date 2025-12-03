def uoc(x):
    t=[]
    for i in range(1,int(x**0.5)+1):
        if x%i==0:
            t.append(i)
            if x//i!=i:
                t.append(x//i)
    return t
f=open("DIVSUM.INP")
f1=open("DIVSUM.OUT","w")
x,y=map(int,f.readline().split())
g=uoc(x)
d=0
for i in g:
    if i<=(y//2) and (y-i) in g and i!=y-i:
        d+=1
f1.write(str(d))
f.close()
f1.close()
