f=open("STYLIST.INP")
f1=open("STYLIST.OUT","w")
n,k=map(int,f.readline().split())
m=0
msbd=99999999999999
for i in range(n):
    sbd=int(f.readline())
    re=0
    for j in range(k):
        a,b,c=map(int,f.readline().split())
        tb=(a+b+c)/3
        re+=tb
    if m<re:
        m=re
        msbd=sbd
    elif m==re:
        if msbd>sbd:
            msbd=sbd
f1.write(str(msbd)+" "+str(round(m,2)))
f.close()
f1.close()