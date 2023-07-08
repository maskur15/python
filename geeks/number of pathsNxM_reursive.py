'n , m is the grid size'
def countPath_recursive(n,m):
    'Recursive solution '
    if n==1 or m==1:
        return  1
    return  countPath(n-1,m)+countPath(n,m-1)
#second approach just store the result in a dictionary s
#so that we can use further
dp ={}
def countPath(n,m):
    if n==1 or m==1:
        return  1
    if (n,m) in dp:
        return dp[(n,m)]
    #memoization
    dp[(n,m-1)]= countPath(n,m-1)
    dp[(n-1,m)]=countPath(n-1,m)
    dp[n,m]= dp[(n,m-1)]+dp[(n-1,m)]

    return dp[n,m]
if __name__ == '__main__':
   while True:
    n,m = map(int,input().split())
    print(countPath(n,m))