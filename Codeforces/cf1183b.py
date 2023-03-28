q = int(input())
while q:
    q -= 1
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    m=min(arr)+k
    for  a in arr:
        if abs(a-m)<=k:
            continue
        else:
            m=-1 ;break
    print(m)