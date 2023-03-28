t=int(input())
while t:
    t-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    while len(a) >=1 and len(b)>=1:
        i=0
        while i<len(a) and  a[i] > b[0]:
            i+=1
        if i==len(a): f=False ; break
        elif a[i] == b[0]:
            a.pop(i)
            b.pop(0)
        elif a[i]<b[i]: f=False ; break
    if len(a)==len(b) and len(a)==0:
        print('YEs')
    else:print("NO")