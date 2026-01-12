def check(x):
    d=-1
    a=x//10
    b=x%10
    d+=a*4
    for i in range(1,b+1):
        if i==1 or i==4 or i==6 or i==9:
            d+=1
    return d
f=open("CAU1.INP")
f1=open("CAU1.OUT","w")
l,r=map(int,f.readline().split())
f1.write(str(check(r)-check(l-1)))
f.close()
f1.close()
d=0
for i in range(34984,94982+1):
    if (i*i-1)%5==0:
        print(i)
print(d)