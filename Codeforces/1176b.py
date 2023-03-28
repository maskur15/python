test = int(input())
while test:
    test-=1
    n=int(input())
    ar=list(map(int,input().split()))
    one=0
    two=0
    ans=0
    for a in ar:
        if a%3==0:
            ans+=1
        elif a%3==1:
            one+=1
        else: two+=1
    if two>one:
        ans+=one
        two=two-one
        ans+=two//3
    else:
        ans+=two
        one=one-two
        ans+=one//3
    print(ans)
