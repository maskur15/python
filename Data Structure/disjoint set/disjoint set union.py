def make_set(v):
    parent[v]=v
    size[v]=1
def find_set(v):
    if v==parent[v]:
        return v
    return find_set(parent[v])
    #parent[v]= find_set(parent[v])
def union_sets(a,b):
    a=find_set(a)
    b=find_set(b)
    if a!=b:
        parent[b]=a
#union by size
def union_setBysize(a,b):
    a=find_set(a)
    b=find_set(b)
    if (a!=b):
        if size[a]< size[b]:
            a,b=b,a
        parent[b]=a
        size[a]+=size[b]
if __name__ == '__main__':
    parent=[0]*10
    size=[0]*10
    print(parent)