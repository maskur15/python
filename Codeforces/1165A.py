arr=[-4,8,15,16,23,42]
inp = input()
c=1
while inp != '':
    inp=int(inp)
    f = False
    k1=0
    k2=0
    while k1<6:
        f=False
        k2=0
        while k2 <6:
            if arr[k1] * arr[k2] == inp:
                f = True
                break
            k2+=1
        if f == True:
            break
        k1+=1
    if f:
        print('? ', k1 + 1, ' ', k2 + 1)
    else:
        print(0)
        break
    c+=1
    inp = input()
    if c==5 and inp.isdigit():
        print(0)
        break
print('! ',(' '.join(list(map(str,arr)))))








