f=open('khoangcach.inp')
f1=open('khoangcach.out','w')
s=f.readline()
q=int(f.readline())
ans=''
for i in range(q):
    mod=26
    dmax=0
    dmin=26
    l,r=map(int,f.readline().split())
    for j in range(l-1,r):
        g=s[j]
        vt=ord(str(g))-97
        if vt>13:
            if dmin==vt:
                dmax=max(dmax,vt)
                mod=0
            else:
                mod=26
            dmin=min(dmin,vt)
        else:
            dmax=max(dmax,vt)
    d=dmax-dmin+mod
    f1.write(str(d)+'\n')

f.close()
f1.close()