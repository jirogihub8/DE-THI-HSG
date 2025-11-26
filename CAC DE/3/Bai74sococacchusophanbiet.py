f1=open('Bai74sococacchusophanbiet.inp')
f2=open('Bai74sococacchusophanbiet.out','w')
l,r=map(int,f1.readline().split())
re='-1'
for i in range(l,r+1):
    s=list(str(i))
    l=list(set(s))
    if len(s)==len(l):
        re="YES"
        break
print(re,i)
f1.close()
f2.close()