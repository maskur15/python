d={1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',
   7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',
17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
t=int(input())
while t:
    t-=1
    n=int(input())
    x=input()
    ans=""
    num=""
    i=len(x)-1
    while i>=0:
        if x[i]=='0':
            num=int(x[i-2])*10+int(x[i-1])
            i=i-2
        else:
            num=int(x[i])
        ans=d[num]+ans
        i-=1
    print(ans)
