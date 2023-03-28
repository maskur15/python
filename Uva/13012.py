while True:
    try:
        n= int(input())
        a=list(map(int,input().split()))
        c=0
        for x in a :
            if x==n: c+=1

        print(c)
    except Exception:
        break