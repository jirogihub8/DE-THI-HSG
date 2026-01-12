
f=open("SANBAY.INP")
f1=open("SANBAY.OUT", "w")

n,x,y,z=map(int,f.readline().split())
a=[0]+list(map(int,f.readline().split()))

inf=10**18
m=max(a)

#dp[i][j] chi phí nhỏ nhất sau tháng i,có j công nhân
dp=[[inf]*(m+1) for _ in range(n+1)]

#vt[i][j] số công nhân tối ưu nhất dùng ở tháng [i-1]
#và dùng [j] công nhân ở tháng [i]
vt=[[-1]*(m+1) for _ in range(n+1)]

# tháng I
for j in range(a[1],m+1):
    dp[1][j]=j*x+j*z
    vt[1][j]=0
# tháng 2 đến tháng n
for i in range(2,n+1):
    for j in range(a[i],m+1):
        for k in range(a[i-1], m+1):

            if k>=j:
                s=(k-j)*y+j*z+dp[i-1][k]
               
            elif k<j:
                s=(j-k)*x+j*z+dp[i-1][k]
            if s<dp[i][j]:
                dp[i][j]=s
                vt[i][j]=k
                

# sa thải lấy chi phí giá nhỏ nhất
ans=inf
end=-1
for j in range(a[n], m+1):
    chiphi=dp[n][j]+j*y
    if chiphi<ans:
        ans=chiphi
        end=j # công nhân j tháng cuối tối ưu
# truy vết
res=''
start=end
for i in range(n,0, -1):
    res+=str(start)+' '
    start=vt[i][start]


f1.write(str(ans)+"\n")
f1.write(res[:-1])

f.close()
f1.close()
