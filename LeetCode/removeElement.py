def solve(ar,val):
    index = 0
    last_index = len(ar)-1
    k=0
    for i in range(len(ar)):
        if ar[i]==val:
            while last_index>=0 and  ar[last_index]==val:
                last_index-=1
            ar[i]= ar[last_index]
            last_index-=1
            k+=1
        if last_index<=0:
            break
    print(ar)
    return  k
if __name__ == '__main__':
    while True:
        ar = list(map(int,input().split()))
        val = int(input())
        solve(ar,val)


