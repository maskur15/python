t=int(input())
while t:
    t=t-1; x=input();  stack=[]
    for a in x:
        stack.append(a) if len(stack)==0 else stack.pop()if a=='B' else stack.append(a)
    print(len(stack))