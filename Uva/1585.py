
t=int(input())
while t:
    t-=1
    x=input()
    c=0
    s=0
    for a in x:
        if a=='O':
           c+=1
           s+=c
        else:c =0
    print(s)