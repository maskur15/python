#I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
def madjacent(i,j):
    c=0
    #up
    if i-1>=0 and ar[i-1][j]=='*': c+=1
    #down
    if i+1<n and ar[i+1][j]=='*': c+=1
    #left
    if j-1>=0 and ar[i][j-1]=='*': c+=1
    #right
    if j+1<m and ar[i][j+1]=='*': c+=1
    #upper left corner
    if i-1>=0 and j-1>=0 and ar[i-1][j-1]=='*': c+=1
    #upper right corner
    if i-1>=0 and  j+1<m and ar[i-1][j+1]=='*': c+=1
    #lower left corner
    if i+1<n and  j-1 >=0 and ar[i+1][j-1]=='*': c+=1
    #lower right cornner
    if i+1<n and  j+1<m and ar[i+1][j+1]=='*': c+=1

    if c==2:
        return True
    else:
        return False
def isLshape(i,j):
   #right up
    if j+1<m and i-1>=0 and ar[i][j+1]=='*' and ar[i-1][j+1]=='*':
        if madjacent(i,j) and madjacent(i,j+1) and madjacent(i-1,j+1):
            ar[i][j]=ar[i][j+1]=ar[i-1][j+1]='.'
            return True
    #right down
    if j + 1 < m and i +1<n  and ar[i][j + 1] == '*' and ar[i+ 1][j + 1] == '*':
        if madjacent(i, j) and madjacent(i, j + 1) and madjacent(i +1, j + 1):
            ar[i][j]=ar[i][j+1]=ar[i+1][j+1]='.'
            return True
    #left up
    if j-1>=0 and i-1>=0 and ar[i][j-1]=='*' and ar[i-1][j-1]=='*':
        if madjacent(i,j) and madjacent(i,j-1) and madjacent(i-1,j-1):
            ar[i][j]=ar[i][j-1]=ar[i-1][j-1]='.'
            return True
    #left down
    if j-1>=0 and i+1<n  and ar[i][j-1]=='*' and ar[i+1][j-1]=='*':
        if madjacent(i,j) and madjacent(i,j-1) and madjacent(i+1,j-1):
            ar[i][j]=ar[i][j-1]=ar[i+1][j-1]='.'
            return True
    #up right
    if i-1>=0 and j+1<m and ar[i-1][j]=='*' and ar[i-1][j+1]=='*':
        if madjacent(i,j) and  madjacent(i-1,j) and madjacent(i-1,j+1):
            ar[i][j]=ar[i-1][j]=ar[i-1][j+1]='.'
            return  True
    #up left
    if i-1>=0 and j-1>=0  and ar[i-1][j]=='*' and ar[i-1][j-1]=='*':
        if madjacent(i,j) and  madjacent(i-1,j) and madjacent(i-1,j-1):
            ar[i][j]=ar[i-1][j]=ar[i-1][j-1]='.'
            return  True
    #down right
    if i+1<n and j+1<m and ar[i+1][j]=='*' and ar[i+1][j+1]=='*':
        if madjacent(i,j) and madjacent(i+1,j) and madjacent(i+1,j+1):
            ar[i][j]=ar[i+1][j]=ar[i+1][j+1]='.'
            return True
    #down left
    if i+1<n and j-1>=0 and ar[i+1][j]=='*' and ar[i+1][j-1]=='*':
        if madjacent(i,j) and madjacent(i+1,j) and madjacent(i+1,j-1):
            ar[i][j]=ar[i+1][j]=ar[i+1][j-1]='.'
            return True
   #left center down
    if j-1>=0 and i+1<n and ar[i][j-1]=='*' and ar[i+1][j]=='*':
        if madjacent(i,j) and madjacent(i,j-1) and madjacent(i+1,j):
            ar[i][j]=ar[i][j-1]=ar[i+1][j]='.'
            return  True
    #left center up
    if j-1>=0 and i-1>=0 and ar[i][j-1]=='*' and ar[i-1][j]=='*':
        if madjacent(i,j) and madjacent(i,j-1) and madjacent(i-1,j):
            ar[i][j]=ar[i][j-1]=ar[i-1][j]='.'
            return  True
    #center up right
    if i-1>=0 and j+1<m and ar[i-1][j]=='*' and ar[i][j+1]=='*':
        if madjacent(i,j) and madjacent(i-1,j) and madjacent(i,j+1):
            ar[i][j]=ar[i-1][j]=ar[i][j+1]='.'
            return  True
    #center down right
    if i+1<n and j+1<m and ar[i+1][j]=='*' and ar[i][j+1]=='*':
        if madjacent(i,j) and madjacent(i+1,j) and madjacent(i,j+1):
            ar[i][j]=ar[i+1][j]=ar[i][j+1]='.'
            return True
    return False


def anti():
    for i in range(n):
        for j in range(m):
            if ar[i][j]=='*':
                if isLshape(i,j):
                    continue
                else: return False
    return True
if __name__ == '__main__':
    test=int(input())
    while test:
        test-=1
        n, m = map(int, input().split())
        ar = list()
        for _ in range(n):
            br = list(input())
            ar.append(br)
        if anti(): print('yes')
        else: print('no')

#is possible!=logic
 # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.


