f=open("DANVU.INP")
f1=open("DANVU.OUT","w")
n,m=map(int,f.readline().split())
A=list(map(int,f.readline().split()))
B=list(map(int,f.readline().split()))
A.sort()
B.sort()
count=0
i=0
j=0 
while i<len(A) and j<len(B):
    if A[i]>B[j]:
        count+=1
        i+=1
        j+=1
    else:
        i+=1
f1.write(str(count))
f.close()
f1.close()
