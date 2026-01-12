f=open("HEXA.INP")
f1=open("HEXA.OUT","w")
n=int(f.readline())
s=str(hex(n))[2:]
s=s.upper()
f1.write(str(s))
f.close()
f1.close()