n=int(input())
x=input()
s=0
for a in x:
    if a=='+':
        s+=1
    else:
        if s>0:
            s-=1
print(s)
