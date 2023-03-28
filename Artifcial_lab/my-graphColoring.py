#graph coloring
n=int(input('Enter number of node: '))
m=int(input("Enter number of color: ")) #number of color
g=[
    [1,1,0,1],
    [1,1,1,1],
    [0,1,1,1],
    [1,1,1,1]
]
x=[0]*n

def isSafe(k,c):
    for i in range(n):
        if g[k][i]==1 and c==x[i]:
            return False
    return True
def graphColor(k):
    for c in range(1,m+1):
        if isSafe(k,c):
            x[k]=c
            if k+1<n:
                graphColor(k+1)
            else:
                print(x)
                return
graphColor(0)
#test case:
#node:4
#color: 3