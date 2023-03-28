#THIS IS PYTHON SOLUTION FOR UVA 12750
#KAFA RAFA AT CHELSA
test=int(input())
for i in range(test):
    n=int(input())
    c=0
    k=1
    ans=0
    while k<=n:
        a=(input())
        if ans==0:
            if a=='W':
                c=0
            else:
                c+=1
            if c==3:
                ans=k
        k+=1
    if ans==0:
        ans="Yay! Mighty Rafa persists!"
    print('Case {}: {}'.format(i+1, ans))



