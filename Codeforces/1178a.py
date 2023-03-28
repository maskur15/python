n=int(input())
x=list(map(int,input().split()))
ans=[1]
num=x[0]
total=sum(x)
for i in range(1,len(x)):
    if x[0]>=2*x[i]:
        num+=x[i]
        ans.append(i+1)
if num*2>total:
    print(len(ans))
    print(' '.join(map(str,ans)))
else: print(0)