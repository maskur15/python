##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
# BY-GK
#caution : 2d list in python
#import sys
#input=sys.stdin.readLine
#x=input().rstrip
#look up:dsu,bfs,dfs,array, dp

import  sys
input=sys.stdin.readline
from collections import defaultdict
# function for adding edge to graph
graph = defaultdict(list)
used=defaultdict()
for i in range(97,97+26):
    used[chr(i)]=False
def addEdge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)
    used[u]=True
    used[v]=True
def bfs(node):
    for v in graph[node]:
        if used[v]:
            used[v]=False
            bfs(v)
if __name__ == '__main__':
    n=int(input())
    for _ in range(n):
        x=input().rstrip()
        for ch in x:
            addEdge(graph,ch,x)
    ans = 0
    for i in range(97, 97 + 26):
        vertex = chr(i)
        if used[vertex]:
            used[vertex] = False
            bfs(vertex)
            ans += 1
    print(ans)

    # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.

