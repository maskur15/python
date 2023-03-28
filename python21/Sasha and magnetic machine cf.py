n = int(input())
x = list(map(int,input().split()))
x.sort()
min = min(x)
sum=sum(x)
s=sum
for a in x:
    for i in range(2,a):
        if(a%i==0):
            t=int(s-min-a+min*i+a/i)
            if t<sum:
                sum=t
print(sum)

