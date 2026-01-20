f=open("choxuan.inp")
f1=open("choxuan.out","w")
a=int(f.readline())
b=int(f.readline())
s=a-b*7
if s>=0:
    f1.write(str(s))
else:
    f1.write(str(-1))
f.close()
f1.close()