f=open("bai2.inp")
f1=open("bai2.out","w")
n=int(f.readline())
for i in f:
    i=i.strip('\n')
    l=0
    r=len(i)-1
    while l<=r:
        if int(i[l])%3==0:
            
            l+=1
        elif int(i[r])%3==0:
            
            r-=1
        elif (int(i[l])+int(i[r]))%3==0:
            
            l+=1
            r-=1
        else:
            break
    print(r-l+1)
f.close()
f1.close()
