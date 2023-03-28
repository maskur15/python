#https://codeforces.com/problemset/problem/1728/C
test=int(input())
while test:
    test-=1
    c=0
    n = int(input())
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    d1 = dict()
    d2 = dict()
    for a in ar1:
        if a in d1:
            d1[a] += 1
        else:
            d1[a] = 1
    for a in ar2:
        if a in d1:
            d1[a] -= 1
            if d1[a] == 0:
                del d1[a]
        else:
            if a in d2:
                d2[a] += 1
            else:
                d2[a] = 1
    d3=dict()
    for a in d1:
        if a>=10:
            v=len(str(a))
            c+=d1[a]
            if v in d3: d3[v]+=d1[a]
            else: d3[v]=d1[a]
        else:
            if a in d3: d3[a]+=d1[a]
            else:  d3[a]=d1[a]
    d4=dict()
    for a in d2:
        if a>=10:
            v=len(str(a))
            c+=d2[a]
            if v in d4: d4[v]+=d2[a]
            else: d4[v]=d2[a]
        else:
            if a in d4 :
                d4[a]+=d2[a]
            else: d4[a]=d2[a]


   # print(d3,d4)
    d5=dict()
    for  a in d3:
        if a in d4:
            if d3[a]==d4[a]:
                del d4[a]
            elif d3[a]>d4[a]:
                d3[a]-=d4[a]
                del d4[a]
                if a  in d5: d5[a]+=d3[a]
                else: d5[a]=d3[a]
            else:
                d4[a]-=d3[a]
        else:
            if a in d5: d5[a]+=d3[a]
            else: d5[a]=d3[a]
    #print(d4,d5)
    for a in d4:
        if a !=1: c+=d4[a]
    for a in d5:
        if a !=1: c+=d5[a]
    print(c)
