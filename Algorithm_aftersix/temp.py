#DIJKSTRA USING HEAPQ
"""
USE THIS AS INPUT
6 7
A B 4
A C 2
B C 5
B D 10
C E 3
D F 11
E D 4
A D
"""
import  heapq
from collections import defaultdict
def shortestPath(graph,src,dest):
    h=[]
    heapq.heappush(h,(0,src))
    path=[]
    while len(h)!=0:
        currcost,crrvtx=heapq.heappop(h)
        if crrvtx==dest:
            print('path exist {} to {} with cost {}'.format(src,dest,currcost))
            break
        for neigh,neighcost in graph[crrvtx]:
            heapq.heappush(h,(currcost+neighcost,neigh))

graph= defaultdict(list)
v,e=map(int,input().split())
for i in range(e):
    u,v,w=map(str,input().split())
    graph[u].append((v,int(w)))
src,dest=map(str,input().split())

shortestPath(graph,src,dest)