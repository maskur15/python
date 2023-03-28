#dfs
node=int(input('Enter the number of nodes : '))
edge=int(input('enter the number of edges : '))
adj=[[]*node for _ in range(node)]
visited=set()
print('Enter {} edges :'.format(edge))
for _ in range(edge):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
root=int(input('Enter the root node : '))
queue=[]
queue.append(root)
visited.add(root)
while len(queue):
    v=queue.pop() #take the last value
    print(v,end=' ')
    for a in adj[v]:
        if a not in visited:
            visited.add(a)
            queue.append(a)
