#zapping
while True:
    x,y =map(int,input().split())
    if x==-1 and y==-1 :
        break
    a=min(x,y)
    b=max(x,y)
    ans1= b-a
    ans2=99-b+1+a
    print(min(ans1,ans2))