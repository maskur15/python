test=int(input())
while test:
    test=test-1
    n = int(input())
    x = input()
    f1 = False
    f2=False
    ans=0
    x=x[n-1]+x
    for i in range(1,n+1):
        if x[i]=='-' or x[i-1]=='-':
            ans+=1
        if x[i]=='>':
            f1=True
        if x[i]=='<':
            f2=True

    if f1 and f2:
         print(ans)
    else:
         print(n)

