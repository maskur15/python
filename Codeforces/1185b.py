n=int(input())
while n:
    n-=1
    x1=input()
    x2=input()
    k=0
    f=True
    i=0
    if len(x1)==len(x2):
            if x1==x2:
                print('YES')
            else:
                print('NO')
    elif len(x1)> len(x2):
        print('NO')
    else:
        while i<len(x2):

            if k<len(x1) and x1[k]==x2[i]:
                k+=1
                i+=1
            elif k-1 >=0 and x1[k-1]==x2[i]:
                i+=1
            else:
                f=False
                break
        if f==False:print('NO')
        elif k==len(x1) and i==len(x2):print('YES')
        else:
            print('NO')

