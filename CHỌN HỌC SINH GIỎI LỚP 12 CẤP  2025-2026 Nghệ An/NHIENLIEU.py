import bisect
f=open("NHIENLIEU.INP")
f1=open("NHIENLIEU.OUT","w")
N=int(f.readline())
a=list(map(int,f.readline().split()))
vt={0:[N+1]}
m=[]
R=[0]*(N+1)
for i in range(N-1,-1,-1):
    vt_min=bisect.bisect_left(m,a[i])
    if a[i] not in m:
        m.insert(vt_min,a[i])

    if a[i] not in vt:
        vt[a[i]]=[i+1]
    else:
        vt[a[i]].insert(0,i+1)
    
        
    print('min của :',a[i],'là',m[vt_min-1])
    if vt_min==0:
        print('khoảng cách từ a[i] đến vị trí của min là:',N-i)
        print("từ",i+1,'đến',N)
        R[i+1]=N
    else:
        print('khoảng cách từ a[i] đến vị trí của min là:',vt[m[vt_min-1]][0]-i-1)
        print("từ",i+1,'đến',vt[m[vt_min-1]][0])
        R[i+1]=vt[m[vt_min-1]][0]
print("-----------------------------------------------------------")
q=int(f.readline())
for i in f:
    L1,R1,x=map(int,i.split())
    L0=L1
    R0=R[L1]
    check=a[L1-1]
    result=0
    checkN=0
    while check !=x and L0<=R1 and checkN!=1:
        L0=R0
        R0=R[L0]
        
        check=a[L0-1]
        if R0==N:
            checkN=1
    
    if check==x:
        if R0==N:
            result=N-L0+1
        elif R0>R1:
            result=R1-L0+1
        elif R0<R1:
            result=R0-L0
        elif R0==R1:
            
            result=R0-L0
    if result==0:
        print("Từ ",L1,"đến ",R1,"thì ",x,"không tồn tại")
    else:
        if R0==N:
            R0+=1
        
        print("Từ ",L1,"đến ",R1,"thì ",x,"trong từ vị trí ",L0,"đến vị trí ",R0-1,)
        print("số lượng ",x,"là ",result)
    
    
    
    
