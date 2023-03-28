t=int(input())

for k in range(1,t+1):
    d=dict()
    m=0
    for i in range(10):
        a,b=input().split()
        b=int(b)
        d[a]=b
        if m<b:
            m=b
    print('Case #{}:'.format(k))
    for v in d:
        if d[v]==m:
            print(v)

