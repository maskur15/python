t=int(input())
for k in range(1,t+1):
    n=int(input())
    a=list(map(int,input().split()))
    h=s=0

    for i in range(1,n):
        if a[i]>a[i-1]: h+=1
        elif a[i]<a[i-1]: s+=1

    print('Case {}: {} {}'.format(k,h,s))