#uva is case sensitive
#careful about the output case lower upper space

count=1
while True:
    try:
        ar = input()
        if len(ar) == 0: break
        print('Case {}:'.format(count))
        index = list()
        c = 0
        index.append(c)
        for i in range(1, len(ar)):
            if ar[i] == ar[i - 1]:
                index.append(c)
            else:
                c += 1
                index.append(c)

        t = int(input())
        count += 1
        for i in range(1, t + 1):
            a, b = map(int, input().split())
            if index[a] == index[b]:
                print('Yes')
            else:
                print('No')

    except Exception:
        break