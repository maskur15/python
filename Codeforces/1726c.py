def main():
    n=input()
    x=input()
    ar=[-1 for _ in range(len(x))]
    stack=list()
    for i in range(len(x)):
        if x[i]==')':
            ch=stack.pop()
            ar[ch]=i
        else:
            stack.append(i)
    c=0
    for v in range(len(ar)):
        if ar[v]!=-1:
            #print('{}: '.format(v),end=' ')
            c+=1
            while v<len(ar) and ar[v]!=-1:
                tv=v
                #print(ar[v],end=' ')
                v=ar[v]+1
                ar[tv]=-1

            #print()
    print(c)

if __name__=='__main__':
    tst=int(input())
    while tst:
        tst-=1
        main()