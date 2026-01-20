S=input().strip()
N=len(S)
S=" "+S   # để dùng chỉ số từ 1
 
# cnt[c][i]=số lần ký tự c xuất hiện trong đoạn [1..i]
cnt=[[0]*(N+1) for _ in range(26)]
result=''
for i in range(1,N+1):
    for c in range(26):
        cnt[c][i]=cnt[c][i-1] 
    cnt[ord(S[i])-97][i]+=1
q=int(input())
for i in range(q):
    L,R=map(int,input().split())
 
    a=[]
    for c in range(26):
        
        if cnt[c][R]-cnt[c][L-1]>0:
            a.append(c)

    m=len(a)
    if m<2:
        result+=str(0)+'\n'
 
    ans=0
    for i in range(m):
        for j in range(i+1,m):
            d=abs(a[i]-a[j])
            d=min(d,26-d)   # khoảng cách vòng tròn
            ans=max(ans,d)
    result+=str(ans)+'\n'
'''for i in result:
    print(i,end='')'''