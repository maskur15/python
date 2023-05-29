from math import  inf
def dijkstra(adj,s):
    n=len(adj)
    dist = [inf  for _ in range(n)]
    dist[s]=0
    visit = [False]*n
    parent = {}
    for i in range(n):
        v =-1
        for j in range(n):
            if visit[j]==False and (v==-1 or dist[j]< dist[v]):
                v = j
        if dist[v]==inf:
            break
        visit[v]=True
        for edge in adj[v]:
            to = edge[0]
            weight = edge[1]
            if dist[v]+weight<dist[to]:
                dist[to]= dist[v]+weight
                parent[to]=v
    print(dist)
    print(parent)

def make_graph():
    pass

from collections import  defaultdict
if __name__ == '__main__':

    n= int(input('Enter number of node : '))
    edge = int(input('Enter number of edges : '))
    print('Enter edges: a,b,weight')
    adj = defaultdict(list)
    for _ in range(edge):
        a,b,weight = map(int,input().split())
        adj[a].append((b,weight))
        adj[b].append((a,weight))
    for node in adj:
        print(adj[node])
    #source vertex is 0
    dijkstra(adj,0)
