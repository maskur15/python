n=int(input())
for i in range(1,n+1):
    x,y,z=map(int,input().split())
    print('Case {}: '.format(i),end='')
    if x<=20 and y<=20 and z<=20:
        print('good')
    else:print('bad')