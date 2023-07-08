
def countPath(n,m):
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][1]=1
    for j in range(m+1):
        dp[1][j]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            if  i!=j:
                dp[i][j]= dp[i-1][j] + dp[i][j-1]
    return dp[n][m]
if __name__ == '__main__':
   while True:
    n,m = map(int,input().split())
    print(countPath(n,m))