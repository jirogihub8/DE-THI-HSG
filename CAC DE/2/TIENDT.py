f=open("TIENDT.INP")
f1=open("TIENDT.OUT","w")
p,t,m=map(int,f.readline().split())
du=p-10
if du<0:
    du=0
if du>0:
    p=10
    
if m==1:
    if 2<=t<=6:
        result=600*p+300*du
    else:
        result=420*p+210*du
else:
    if 2<=t<=6:
        result=900*p+450*du
    else:
        result=630*p+315*du
print(result)`