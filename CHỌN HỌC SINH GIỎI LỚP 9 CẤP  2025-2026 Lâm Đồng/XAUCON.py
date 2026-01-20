f=open("xaucon.inp")
f1=open("xaucon.out","w")
n=" "+f.readline()
vt=[0] 
nguyen_am={"u","e","o","a","i"}
for i in range(len(n)):
    if n[i] in nguyen_am:
        vt.append(i)
result=0
for i in range(1,len(vt)):
    result+=(vt[i]-vt[i-1]-1)*2
print(result)


