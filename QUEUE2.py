t=int(input())
for x in range(t):
    n,m,k,l=map(int,input().split())
    a=list(map(int,input().split()))
    a.sort()
    time=[]
    f=(m+1)*l
    g=0
    for y in a:
        f=f-(y-g)+l
        time.append(f)
        g=y
    time.append(f-(k-g)+l)
    print(min(time)-l)
