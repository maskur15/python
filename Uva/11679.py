#check wheheter the each bank has a debit at the end
#of all tranasaction

while True:
    b, n = map(int, input().split())
    if b==0 and n==0:
        break
    reserve = list(map(int, input().split()))
    for _ in range(n):
        d, c, v = map(int, input().split())
        reserve[d - 1] -= v
        reserve[c - 1] += v
    ans='S'
    for v in reserve:
        if v < 0:
            ans='N'
            break
    print(ans)