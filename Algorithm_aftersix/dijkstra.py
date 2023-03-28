#dijkstra algorithm
#finding shortest path from a single vertex to all
#other vertex wehere all vertex have positive weight

from math import sqrt
from queue import PriorityQueue
import numpy as np
import math
def add_value(s_dict,key,value):
    if key not in s_dict:
        s_dict[key]=list()
    s_dict[key].append(value)
    return  s_dict
def set_priorityValue(n):
    weight=PriorityQueue()
    for i in range(n+1):
        weight.put((i,math.inf))
    return  weight
def show_priority(weight):
    while not weight.empty():
        print(weight.get())
#number of vertices and edges
graph={}
print('Enter the number of vertices and edges: ')
n,m=map(int,input().split())
array=np.zeros((n,n))
weight= set_priorityValue(n)
show_priority(weight)
print('Enter the starting vertex: ')
v=int(input())

print('Enter edeges a to b and weight: ')
for i in range(m):
    a,b,w=map(int,input().split())
    graph=add_value(graph,a,b)
    graph=add_value(graph,b,a)

for i in graph:
    print(i,end=' ->')
    for j in graph[i]:
        print(j,end=' ')
    print()


print(graph)
