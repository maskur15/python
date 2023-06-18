def bigMod(b,p,m):
    if p==0:
        return 1
    if p==1:
        return b%m
    result = bigMod(b*b,p//2,m)
    if p%2==0:
        return  result%m
    else:
        return (b*result%m )%m
if __name__ == '__main__':

    while True:
        try:
            b = (input())
            p = int(input())
            m = int(input())
            x= input()
            print(bigMod(b,p,m))
        except Exception:
            break
