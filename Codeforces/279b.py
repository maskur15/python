n, time = map(int, input().split())
x = list(map(int, input().split()))
i = c = 0
sum = ans = index = 0
while i < len(x) and index < len(x):
    if sum + x[i] <= time:
        sum += x[i]
        c += 1
    else:
        sum -= x[index]
        index += 1
        i -= 1
        ans = max(ans, c)
        c -= 1
    i += 1
print(max(c, ans))
