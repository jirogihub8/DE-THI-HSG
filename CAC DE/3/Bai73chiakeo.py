f1=open('Bai73chiakeo.inp')
f2=open('Bai73chiakeo.out','w')
T=int(f1.readline())
for i in range(T):
    a,b,c,d=list(map(int,f1.readline().split()))
    s=(a+b+c+d)
    if s%2==0:
        s=s%2
        if (a+b)==(c+d) or (a+c)==(b+d) or (a+d)==(b+c):
            print("YES")
        else:
            print('NO')
    else:
        print("NO")
        
f1.close()
f2.close()
