def digit(x,c):
    if str(len(x))==x:
        return c

    return digit(str(len(x)),c+1)

while True:
    x=input()
    if x=='END':
        break
    print(digit(x,0)+1)