# m-coloring
from collections import defaultdict
n = int(input('Enter number of node: '))
color = int(input('Enter number of color: '))
edge = int(input('Enetr number of edge: '))
print('Enter edges : ')
g = defaultdict(set)
# adding edges with iteself
for i in range(n + 1):
    g[i].add(i)
for _ in range(edge):
    x, y = map(int, input().split())
    g[x].add(y)
    g[y].add(x)
nodeColor = [0 for _ in range(n + 1)]

def isSafe(node, clr):
    for v in g[node]:
        if nodeColor[v] == clr:
            return False
    return True


def mColor(nthNode):
    if nthNode == 0:
        return True
    for c in range(1, color + 1):
        if isSafe(nthNode, c):
            nodeColor[nthNode] = c
            if mColor(nthNode - 1):
                return True
            nodeColor[nthNode] = 0
    return False


if __name__ == '__main__':

   if  mColor(n):
    print(nodeColor)
   else:
       print('not possible')

# test case:
# node:5
# color:3
# edge: 5
# edges:
# 1 2
# 1 3
# 2 4
# 2 5
# 3 5

