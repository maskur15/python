def add(n,m):
    return n+m
def mix(x,y,function):
    return x*y+function(x,y)
res=mix(3,4,add)
print(res)