#bfs
node=int(input('Enter the number of node : '))
edge=int(input(('Enter the numebr of edges : ')))
print('Enter the edges like a to b : ')
adj=[[]*node for _ in range(node)]
for  _ in range(edge):
    a,b=map(int,input().split())
    adj[a].append(b)
    adj[b].append(a)
start=int(input('Enter root node : '))
visittd=set()
visittd.add(start)
queue=[]
queue.append(start)
while len(queue):
    v=queue.pop(0) #pop the first element
    print(v,end=' ')
    for a in adj[v]:
        if a not in visittd :
            visittd.add(a)
            queue.append(a)

