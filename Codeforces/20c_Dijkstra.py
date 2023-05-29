#Fresh dijkstra
from collections import  defaultdict
from math import  inf
class priorityList(list):
    adj = list()
    def add(self,value):
        pass
def dijkstra(adj,s,d):
    n=len(adj)+1
    visit =[False]*n
    dist = [inf]*n
    dist[s]=0
    parent ={}
    parent[s]=s
    for i in range(1,n):
        v = -1
        for j in range(1,n):
            if v==-1 and visit[j]==False:
                v=j
            elif v!=-1 and visit[j]==False and dist[v]> dist[j]:
                v =j
        if v==-1 or  dist[v]==inf :
            break
        visit[v]=True
        for node in adj[v]:
            if dist[node[0]]> dist[v]+node[1]:
                dist[node[0]]= dist[v]+ node[1]
                parent[node[0]]=v

    print(dist)
    path =[]
    while True:
        path.append(s)
        s=parent[s]
        if d==s:
            path.append(s)
            break
    print(path)
class Graph:
    adj = defaultdict(list)
    def addEdge(self,a,b,weight):
        self.adj[a].append((b,weight))
        self.adj[b].append((a,weight))
    def show_Edge(self):
        for node in self.adj:
            print(node,self.adj[node])


if __name__ == '__main__':
    n,m = map(int,input().split())
    g = Graph()
    for _ in range(m):
        a,b,w = map(int,input().split())
        g.addEdge(a,b,w)
    g.show_Edge()
    dijkstra(g.adj,1,n)