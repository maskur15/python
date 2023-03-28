#https://codeforces.com/contest/25/problem/D
#use disjoint set union
#https://www.youtube.com/watch?v=wU6udHRIkcc&ab_channel=AbdulBari

##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
def find_parent(a):
    if ar[a]==-1:
        return a
    return find_parent(ar[a])

if __name__ == '__main__':
    n=int(input())
    ar=[-1]*(n+1)
    road=[]
    cycle=list()
    for _ in range(1,n):
        a,b=map(int,input().split())
        p1=find_parent(a)
        p2=find_parent(b)
        if p1==p2 :
            cycle.append((a,b))
        else:
            ar[p1]=p2
    for i in range(1,n+1):
        if ar[i]==-1:
            road.append(i)
    print(len(cycle))
    root=road.pop()
    for i in range(len(cycle)):
        x,y=cycle.pop()
        print(x,y,root,road.pop())

    # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
