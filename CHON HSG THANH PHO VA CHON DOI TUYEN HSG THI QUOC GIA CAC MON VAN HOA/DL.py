import bisect
with open("DL.INP",'r') as f:
    S = f.readline()
    l = len(S)
with open("DL.OUT","w") as f:
    V = [0]
    D = [0]
    v = 0
    d = 0
    for i in S:
        if i == 'V':
            v += 1
        else:
            d += 1
        V += [max(V[0],v)]
        D += [max(D[0],d)]
    for i in range(1,len(V)):
        if V[i]//2==V[i]/2:
            c = V[i]//2
            j = bisect.bisect_left(D,c)
            
     
