tst=int(input())
while tst:
    tst-=1
    input()
    n, m = map(int, input().split())
    vt = list()
    dictionary = dict()
    for i in range(1, m + 1):
        x, w = map(int, input().split())
        dictionary[x] = i
        vt.append((x, w))
    # sort by the second element of tuple using x index 1
    vt.sort(key=lambda x: x[1])
    sum = 0
    arr = list()
    for i in range(0, n * 2):
        arr.append(vt[i][0])
        sum += vt[i][1]
    arr.sort()
    print(sum)
    for i in range(1, n + 1):
        print(dictionary[arr[i - 1]], ' ', dictionary[arr[n * 2 - i]])

