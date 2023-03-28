
if __name__=='__main__':

    test = int(input())
    while test:
        test-=1
        n,k= map(int,input().split())
        health = list(map(int,input().split()))
        power = list(map(int,input().split()))
        d = dict()
        for i in range(n):
            if power[i] in d:
             d[power[i]]= max(d[power[i]],health[i])
            else:
                d[power[i]]=health[i]
        d=dict(sorted(d.items()))
        i=0
        s=k
        f='YES'
        pre=None
        for key in d:
            if pre and  pre!=key:
                if d[key]>s:
                    k-=key
            pre=key
            while d[key]>s:
                d[key]-=s
                if d[key]<=0:
                    break
                k=k-key
                if k<=0:
                    f='NO'
                    break
                s+=k
            if f=='NO': break


        print(f)

'''
I'odnt 'no'
'''