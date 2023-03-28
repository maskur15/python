def seq(num):
    ant = [i for i in range(10)]
    dif1= list()
    dif2=list()
    ans1=list()
    for i in range(4):
        dif1.append(3-i)
    for v in dif1:
        for i in range(10):
            for j in range(10):
                if i+j==v:
                    ans1.append((i,j,3-i-j))
    for i in range(10):
        dif2.append(13-i)
    ans2=list()
    for v in dif2:
        for i in range(10):
            for j in range(10):
                if i+j==v:
                    ans2.append((i,j,13-i-j))

    ans3=list()
    dif3=list()
    for i in range(10):
        dif3.append(23-i)
    for v in dif3:
        for i in range(10):
            for j in range(10):
                if i+j==v:
                    ans3.append((i,j,23-i-j))

    ans=ans1+ans2+ans3
    for a in ans:
        a1=a[0]
        a2=a[1]
        a3=a[2]
        if a1==a2 and a1==a3:
            if num[a1]>=3:
                return True
        elif a1==a2:
            if num[a1]>=2 and num[a3]>=1:
                return True
        elif a1==a3:
            if num[a1]>=2 and num[a2]>=1:
                return True
        elif a2==a3:
            if num[a2]>=2 and num[a1]>=1:
                return True
        else:
            if num[a1]>=1 and num[a2]>=1 and num[a3]>=1:
                return True
    return False

test=int(input())
while test:
    test-=1
    n=int(input())
    ar=list(map(int,input().split()))
    num ={i:0 for i in range(10)}
    for v in ar:
        num[v%10]+=1
    if seq(num):
        print('yes')
    else: print('no')
#This is the favour of Allah. He grants it to whoever He wills. And Allah is the Lord of infinite bounty.
