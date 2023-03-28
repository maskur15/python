def find_parent(v):
    if parent[v]==-1:
        return v
    return find_parent(parent[v])
if __name__ == '__main__':
    #enter number of node.nodes are numbered from 1 to n
    print('Enter number of node :')
    n=int(input())
    #all node set to -1 which means each node is its own parent
    parent=[-1]*(n+1)
    print('Enter number of edge : ')
    edge=int(input())
    print('Enter edges : ')
    cycle=list()
    for _ in range(edge):
        #a to b edges
        a,b=map(int,input().split())
        p1=find_parent(a)
        p2=find_parent(b)
        if p1==p2:
            #means both have same parent . so there is a cycle
            cycle.append((a,b))
        else:
            #both a and b are in different set .
            #merge this two set in a single set and make any one its parent of ohters one
            parent[p1]=p2
    #finally we have the graph which contain the connected component without cycle
    #so the parent which have value -1 are the root node
    #number of -1 represnets the connected componennt in the graph
    print('connected componnet: ',parent.count(-1)-1)# minus 1 because we defnine the parent array from 0 to n
    print('Number of cylcel: ',len(cycle))
    print('cycles are : ')
    for c in cycle: print(c)
