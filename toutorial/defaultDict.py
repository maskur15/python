##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
# BY-GK
from collections import defaultdict
# function for adding edge to graph
graph = defaultdict(set)
used=defaultdict()

def addEdge(graph, u, v):
    graph[u].add(v)
    graph[v].add(u)

if __name__ == '__main__':
   addEdge(graph,3,43)
   addEdge(graph,2,4)
   addEdge(graph,2,5)
   addEdge(graph,1,34)
   print(graph)
   for g in graph:
      for v in graph[g]:
          print(v)


    # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.

