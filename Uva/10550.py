while True:
    a, b, c, d = map(int, input().split())
    if a==b and b==c and c==d and c==0:
        break
    x1 = x2 = 0
    x3 = 0
    #clock wise
    if a < b:
        x1 = 40 - b + a
    else:
        x1 = a - b
    #counter clockwise
    if b > c:
        x2 = 40 - b + c
    else:
        x2 = c - b
    #clock wise
    if c < d:
        x3 = 40 - d + c
    else:
        x3 = c - d
    print(1080+(x1+x2+x3)*9)