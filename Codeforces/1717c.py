
def solve(a,b):
    ans=True
    for i in range(len(b)):
        if a[i]==b[i]:
            continue
        elif a[i]>b[i]:
            ans=False
            break
        else:
            if i==len(b)-1:
                if(b[i]>b[0]+1):
                    ans=False; break
            else:
                if b[i]>b[i+1]+1:
                    ans=False ; break
    return ans
test=int(input())
while  test:
    test-=1
    n=int(input())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    if solve(a,b):print('yes')
    else:print('no')