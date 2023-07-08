'n , m is the grid size'
def countPath(n,m):
    'Recursive solution '
    if n==1 or m==1:
        return  1
    return  countPath(n-1,m)+countPath(n,m-1)
if __name__ == '__main__':
   while True:
    n,m = map(int,input().split())
    print(countPath(n,m))