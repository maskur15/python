import sys
while True:

    try:
        n, m = map(int, input().split())
        c = 0
        while n:
            n -= 1
            match = list(map(int, input().split()))

            result = 1
            for score in match:
                if score == 0:
                    result = 0
            c += result
        print(c)

    except Exception:
        quit()
