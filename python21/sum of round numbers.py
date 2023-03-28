t=int(input())
while t>=1:
    t-=1
    x=input()
    n=x.count('0')
    print(len(x)-n)
    for i in range(len(x)):
        if x[i]!='0':
            print(x[i]+'0'*(len(x)-i-1),end=" ")
    print()
