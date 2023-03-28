t=int(input())
while t:
    t-=1
    n=int(input())
    x=input()
    i=0
    c=0
    while i < len(x):
        if x[i]=='(' or (x[i]==')' and x[i+1]==')'):
            i=i+2
            c+=1
            if i <len(x):
                x=x[i:]
                i=0
            else:
                x="";
                break
        else:
            i=i+1
            cx=0

            while i<len(x) and x[i]!=')':
                cx+=1
                i=i+1
            if i==len(x):
                c+=cx//2
                if(cx%2!=0):
                    x=")("
                break
            else:
                c+=1
                i=i+1
                if i < len(x):
                    x = x[i:]
                    i=0
                else:
                    x = ""
                    break
    print(c,' ',len(x),' ',x,' ',i)
