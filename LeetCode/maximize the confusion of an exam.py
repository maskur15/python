def solve(answer,k,cr):
    i=0
    c=0
    ans=0
    j=0
    f='T'
    if cr=='T':
        f='F'
    for i in range(len(answer)): 
        if answer[i]==cr:
            continue
        else:
            c+=1
            if c==k+1:
                ans = max(ans,i-j)
                c-=1
                while j < len(answer) and answer[j]!=f:
                    j+=1
                j+=1
    if ans ==0:
        ans = len(answer)
    ans = max(ans,len(answer)-j)

    return  ans

def getSolve(ar,k):
    t1 =solve(ar,k,'T')
    t2= solve(ar,k,'F')

    return max(t1,t2)
if __name__ == '__main__':
    while True:
        ar = input()
        k= int(input())
        print(getSolve(ar,k))
