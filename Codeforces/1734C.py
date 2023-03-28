test=int(input())
while test:
    test-=1
    n = int(input())
    x = input()
    x = "A" + x + "B"
    cost = 0
    count=0
    l = list()

    for i in range(1, n + 1, 1):

        if  x[i] == '0':
            if i not in l:
                l.append(i)
                count+=1
                cost += i
                c = 2
                while i * c <= n and x[i * c] == '0':
                    if i*c in l:
                        c+=1
                    else:
                        cost += i
                        l.append(i * c)
                        c += 1
            else:
                c = 2
                while i * c <= n and x[i * c] == '0':
                    if i*c in l:
                        c+=1
                    else:
                        cost += i
                        l.append(i * c)
                        c += 1
    print(cost)



