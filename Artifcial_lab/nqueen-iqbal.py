def is_attack(i,j):
    for l in range(n):
        for m in range(n):
            if board[i][m]==1 or board[l][j]==1 or (i+j==l+m and board[l][m]==1) or (i-j==l-m and board[l][m]==1):
                return True
    return False
def nqueen(queen):
    if queen==0:
        return True
    for i in range(n):
        for j in range(n):
            if is_attack(i,j)==False and board[i][j]==0:
                board[i][j]=1

                if(nqueen(queen-1)):
                    return True
                board[i][j]=0
    return False
if __name__ == '__main__':
    n = int(input('Enter number of queen: '))
    board = [[0]*n for _ in range(n)] #genrating 2d array
    if nqueen(n):
        for a in board:
            print(a)
    else:
        print('Not possible')