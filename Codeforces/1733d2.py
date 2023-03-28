def main():
    n, x, y = map(int, input().split())
    x1 = input()
    x2 = input()
    c=0
    a=-1
    b=-1
    tc=-1
    for i in range(len(x1)):
        if x1[i]!=x2[i]:
            c+=1
            if a==-1:
                a=i
            elif b==-1:
                b=i
    i=0
    f=0
    prein=-1
    sum=0
    while i<len(x1):
        if x1[i]!=x2[i]:
            f+=1
            if f==1:
                prein=i
            else:
                f=0
                sum+= min((i-prein)*x,y)
        i+=1


    if c%2==0:
        #when  y is minimum
        if y<x:
            if c==2:
                if a+1==b:
                   print(min(x,2*y))
                else: print(y)
            else:
                print(c//2*y)
        else:
            print(sum)
    else:
        print(-1)

if __name__ == '__main__':
    tst=int(input())
    while tst:
        tst-=1
        main()