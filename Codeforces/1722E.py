##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
def solveDp():
    for i in range(1,1002):
        for j in range(1,1002):
            if (i,j) in present:
                    dp[i][j]=present[(i,j)]*i*j + dp[i-1][j] + dp[i][j-1]-dp[i-1][j-1]
            else:
                dp[i][j]= dp[i-1][j]+dp[i][j-1]-dp[i-1][j-1]
if __name__ == '__main__':
    tst=int(input())
    while tst:
        tst-=1
        dp=list()
        for i in range(1005):
            a=[0]*1005
            dp.append(a)
        present=dict()
        n,q=map(int,input().split())
        for _ in range(n):
            a,b=map(int,input().split())
            if (a,b) in present: present[(a,b)]+=1
            else: present[(a,b)]=1
        solveDp()
        for _ in range(q):
            a,b,c,d=map(int,input().split())
            print(max(0,dp[c-1][d-1]-dp[c-1][b]-dp[a][d-1]+dp[a][b]))
 # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.

