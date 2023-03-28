test = int(input())
while test:
    test-=1
    n=int(input())
    x=input()
    x=x+'2'
    c=1
    s=0
    ch=x[0]
    for i in range(1,n+1):
        if x[i]==ch:
            c+=1
        else:
            s+=min(c,2)
            c=1
            ch=x[i]
    print(s-1)