q = int(input())
while q:
    q -= 1
    charge, n, a, b = map(int, input().split())
    c = 0
    temp = charge
    for i in range(n):
        if charge > a:
            c += 1
            charge -= a
        elif charge > b and b < a:
            charge = charge - b
        elif charge <= a and charge <= b:
            charge = -1
            break
    if charge >= 1:

        print(c)
    else:
        print(-1)
