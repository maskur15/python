def isvalid(s):
    x=list()
    x.append(s[0])
    for i in range(1,len(s)):
        ch=s[i]
        if len(x)==0:
            x.append(ch)
            continue
        c=x[len(x)-1]
        if  c=='(' and ch==')':
            x.pop()
        elif c=='{' and ch=='}':
            x.pop()
        elif c=='[' and ch==']':
            x.pop()
        else:
            x.append(ch)
    if len(x)==0:
        return  True
    return False

print(isvalid("{()[{[]}]}()()))"))