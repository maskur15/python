def swap(a,b):
    t=a
    a=b
    b=t
    return  a,b

n, m = map(int, input().split())
arr1 = []
arr2 = []
for i in range(n * 2):
    a = list(map(int, input().split()))
    if i < n:
        arr1.append(a)
    else:
        arr2.append(a)
f=True
for i in range(n):
    for j in range(m-1):
        if arr1[i][j]>= arr1[i][j+1] or arr2[i][j]>= arr2[i][j+1]:
            arr1[i][j],arr2[i][j]=swap(arr1[i][j],arr2[i][j])
            if arr1[i][j] >= arr1[i][j + 1] or arr2[i][j] >= arr2[i][j + 1]:
                f=False; break
    if f==False: break
for i in range(n-1):
    for j in range(m):
        if arr1[i][j]>= arr1[i+1][j] or arr2[i][j]>= arr2[i+1][j]:
            arr1[i][j],arr2[i][j]=swap(arr1[i][j],arr2[i][j])
            if arr1[i][j] >= arr1[i + 1][j] or arr2[i][j] >= arr2[i + 1][j]:
                f = False
                break

    if f == False: break
if f: print('Possible')
else: print('Impossible')
