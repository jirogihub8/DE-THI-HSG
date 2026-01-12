f=open("STICKER.INP")
f1=open("STICKER.OUT","w")
n,x,k=map(int,f.readline().split())
x=x-n*k
f1.write(str(x//n)+' '+str(n-x%n))
f.close()
f1.close()
