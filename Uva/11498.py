while True:
    k=int(input())
    if k==0:
        break
    m,n=map(int,input().split())
    while k:
        k-=1
        x,y=map(int,input().split())
        if x==m or y==n: print('divisa')
        elif x>m and y>n : print('NE')
        elif x<m and y>n : print('NO')
        elif x>m and y<n : print('SE')
        else:print('SO')