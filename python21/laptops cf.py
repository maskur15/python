n=int(input())
x=[None]*222222
for i in range(1,n+1):
    a,b=map(int,input().split())
    x[a]=b
for i in range(1,n):
    if x[i]>x[i+1]:
        print("Happy Alex")
        exit()
print("Poor Alex")