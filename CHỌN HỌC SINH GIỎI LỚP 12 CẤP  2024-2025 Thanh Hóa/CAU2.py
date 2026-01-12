def check(x):
    m=0
    d=0
    for i in x:
        if i not in "ANH":
            d+=1
        else:
            if m<d:
                m=d
            d=0
    if d!=0:
        if m<d:
            m=d
    if m==0:
        m=-1
    return m

        
f=open("CAU2.INP")
f1=open("CAU2.OUT","w")
T=int(f.readline())
for i in range(T):
    a=f.readline()
    f1.write(str(check(a))+'\n')
f.close()
f1.close()
            
    
