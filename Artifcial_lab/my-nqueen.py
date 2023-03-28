#2d array be cautious
n=int(input('Enter number of queen : '))
board=[[0]*n for _ in range(n)]
def is_attack(i,j):
    for l in range(n):
        for m in range(n):
            if (l==i or m==j or l+m==i+j or l-m==i-j) and board[l][m]==1:
                return True
    return False
def solveQueen(qnleft):
    if qnleft==0:
        return True
    for i in range(n):
        for j in range(n):
            if not(is_attack(i,j)) and board[i][j]==0:
                board[i][j]=1
                if solveQueen(qnleft-1):
                    return True
                board[i][j]=0

if __name__ == '__main__':
    if solveQueen(n):
        for a in board:
            print(a)
    else:
        print('Not possible')