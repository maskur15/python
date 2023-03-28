n=int(input('Enter number of node : '))
edge=int(input('Enter number of edge: '))
g=[[]*n for _ in range(n)]
for i in range(edge):
    x,y=map(int,input().split())
    g[x].append(y)
    g[y].append(x)

for i in range(n):
    print(i,": ",g[i])