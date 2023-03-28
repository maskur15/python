
if __name__=='__main__':

    n,m=map(int,input().split())
    x=list(map(int,input().split()))

    s=0
    arr=list()
    c=0
    ans=list()
    for a in x:
        s=s+a
        c=0
        sum=s
        for v in arr:
            if sum<=m:
                break
            sum=sum-v
            c+=1
        ans.append(c)
        arr.append(a)
        arr.sort(reverse=True)

    for a in ans:
        print(a , end=' ')
