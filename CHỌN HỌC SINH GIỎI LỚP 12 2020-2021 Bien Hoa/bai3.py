f=open("bai3.inp")
f1=open("bai3.out","w")
n=int(f.readline())
x1=x4=y3=y4=-99999999
y1=y2=x2=x3=99999999
for i in f:
    a,b=i.split()
    a,b=int(a),int(b)
    x1,y1=max(a,x1),min(b,y1)
    x2,y2=min(a,x2),min(b,y2)
    x3,y3=min(a,x3),max(b,y3)
    x4,y4=max(a,x2),max(b,y4)
f1.write(str(x1)+' '+str(y1)+'\n')
f1.write(str(x2)+' '+str(y2)+'\n')
f1.write(str(x3)+' '+str(y3)+'\n')
f1.write(str(x4)+' '+str(y4)+'\n')
f.close()
f1.close()

