from copy import deepcopy
ar=[[1,2,4],[2,4,2]]
a=deepcopy(ar)
a[1][1]=333
print(a)
print(ar)