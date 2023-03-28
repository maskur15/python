try:
    #if the slash is odd then the . is inside the polygon

    while True:

        h, w = map(int, input().split())
        ans = 0
        square=0
        ar = list()
        for _ in range(h):
            s = list(input())
            ar.append(s)
        for i in range(0,h,1):
            slash=0
            for j in range(0,w,1):
                if ar[i][j]=='/' or ar[i][j]=='\\':
                    ans+=1
                    slash+=1
                elif slash%2!=0:
                    square+=1
        print(ans//2+square)
except Exception:
    quit()