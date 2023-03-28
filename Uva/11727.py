n = int(input())
for i in range(1, n + 1):
    x, y, z = map(int, input().split())
    a = max(x, y, z)
    b = min(x, y, z)
    print('Case {}: '.format(i), end='')
    if y > b and y < a:
        print(y)
    elif x > b and x < a:
        print(x)
    else:
        print(z)
