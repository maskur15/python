n=int(input())
while n:
    n-=1
    ar=input()
    m=f=0
    if len(ar)<=4:
        print('NO LOOP')
        continue
    for a in ar:
        if a=='M': m+=1
        elif a=='F': f+=1
    if m==f: print('LOOP')
    else: print('NO LOOP')
