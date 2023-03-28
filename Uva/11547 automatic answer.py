t=int(input())
while t:
    t-=1
    n=int(input())
    n=((n*567/9+7492)*235/47)-498
    n=abs(int(n))

    n=n//10
    print(n%10)
