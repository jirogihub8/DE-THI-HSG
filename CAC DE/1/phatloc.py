

f=open("PHATLOC.INP")
f1=open("PHATLOC.OUT","w")
T=int(f.readline())
d=0
for i in f:
    l,r=map(int,i.split())
    for i in range(000,6000):
        if '6' in str(i):
            d+=1
f.close()
f1.close()

    