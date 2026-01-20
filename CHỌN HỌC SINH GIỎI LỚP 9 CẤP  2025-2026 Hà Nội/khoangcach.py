'''def build(idx,l,r):    
    m=(l+r)//2
    if l==r:
        tmin[idx] = a[l]
        tmax[idx] = a[l]
        return

    build(idx*2,l,m)
    build(idx*2+1,m+1,r)
    tmin[idx]=min(tmin[idx*2],tmin[idx*2+1])
    tmax[idx]=max(tmax[idx*2],tmax[idx*2+1])
def get(idx,l,r,u,v):
    if v<l or u>r:
        return [999,-999]
    if u<=l and r<=v:
        return [tmin[idx],tmax[idx]]
    m=(l+r)//2
    left=get(idx*2,l,m,u,v)
    right=get(idx*2+1,m+1,r,u,v)
    return [min(left[0],right[0]),max(left[1],right[1])]


f=open("khoangcach.inp")
f1=open("khoangcach.out","w")
m=f.readline().strip('\n')
q=int(f.readline())
print(m)
a=""
for i in m:
    a+=str(ord(i)-97)+' '
a=[0]+list(map(int,a.split()))

n=len(a)-1
tmin=[0]*(4*n)
tmax=[0]*(4*n)
build(1,1,n)
for i in range(q):
    l,r=map(int,f.readline().split())
    u,v=get(1,1,n,0,r)
    print(u,v)
    result=max(v-u,26-(v-u))'''
# ================= SEGMENT TREE =================

def build(idx, l, r):
    if l == r:
        t[idx][a[l]] = 1
        return
    m = (l + r) // 2
    build(idx * 2, l, m)
    build(idx * 2 + 1, m + 1, r)
    for i in range(26):
        t[idx][i] = t[idx * 2][i] + t[idx * 2 + 1][i]


def get(idx, l, r, u, v):
    if v < l or r < u:
        return [0] * 26
    if u <= l and r <= v:
        return t[idx][:]
    m = (l + r) // 2
    left = get(idx * 2, l, m, u, v)
    right = get(idx * 2 + 1, m + 1, r, u, v)
    res = [0] * 26
    for i in range(26):
        res[i] = left[i] + right[i]
    return res


# ================= MAIN =================

f = open("khoangcach.inp")
f1 = open("khoangcach.out", "w")

s = f.readline().strip()
q = int(f.readline())

# đổi ký tự thành số 0..25
a = [0]
for ch in s:
    a.append(ord(ch) - 97)

n = len(a) - 1

t = [[0] * 26 for _ in range(4 * n)]
build(1, 1, n)
f1.write(str(t))
for _ in range(q):
    l, r = map(int, f.readline().split())
    cnt = get(1, 1, n, l, r)

    letters = []
    for i in range(26):
        if cnt[i] > 0:
            letters.append(i)

    ans = 0
    k = len(letters)
    for i in range(k):
        for j in range(i + 1, k):
            d = abs(letters[i] - letters[j])
            dist = min(d, 26 - d)
            if dist > ans:
                ans = dist

    f1.write(str(ans ) + "\n")

f.close()
f1.close()
