c=False
while True:
    try:

        given = dict()
        received = dict()
        t = int(input())
        name = list(input().split())
        for a in name:
            given[a] = 0
            received[a] = 0
        while t:
            t -= 1
            balance = list(input().split())
            presentor = balance[0]
            amount = int(balance[1])
            people = int(balance[2])
            if people == 0:
                continue
            evenly_amount = amount // people
            given[presentor] += evenly_amount * people
            for i in range(3, len(balance)):
                received[balance[i]] += evenly_amount
        if c: print()
        c=True
        for a in name:
            print(a, received[a] - given[a])

    except Exception:
        break