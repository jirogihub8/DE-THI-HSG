
f=open("CAPSO.INP")
f1=open("CAPSO.OUT","w")
a=int(f.readline())

s=0
for i in range(1,a+1):
    s+=a//i
f1.write(str(s))
f.close()
f1.close()