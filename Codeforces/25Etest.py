##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
def Leftanti(x1,x2):
    ch=ord(x2[len(x2)-1])- ord('a')
    l=len(d[ch])
    for i in range(l-1,-1,-1):
        index1=d[ch][i]
        index2 = len(x2) - 1
        while index1>=0 and index2>=0:
            if x1[index1]==x2[index2]:
                index1-=1
                index2-=1
            else:
                break
        if index2==-1: return 0
        if index1==-1: return index2+1
    return len(x2)

def Rightanti(x1,x2):
    ch= ord(x2[0])-ord('a')
    l=len(d[ch])
    for i in range(l):
        index1=d[ch][i]
        index2=0
        while index1<len(x1) and index2<len(x2):
            if x1[index1]==x2[index2]:
                index1+=1
                index2+=1
            else:
                break
        if index2==len(x2): return  len(x2)
        if index1==len(x1): return index2
    return 0
def compare(x1,x2,x3):
    t1, t2, t3 = x1, x2, x3
    l1 = len(x1)
    l2 = len(x2)
    l3 = len(x3)
    if l1 >= l2 and l1 >= l3:
        t1 = x1
        if l2 >= l3:
            t2 = x2
            t3 = x3
        else:
            t2 = x3
            t3 = x2
    elif l2 >= l1 and l2 >= l3:
        t1 = x2
        if l1 >= l3:
            t2 = x1
            t3 = x3
        else:
            t2 = x3
            t3 = x1
    elif l3 >= l2 and l3 >= l1:
        t1 = x3
        if l2 >= l1:
            t2 = x2
            t3 = x1
        else:
            t2 = x1
            t3 = x2

    return  t1,t2,t3
if __name__ == '__main__':
        x1=input()
        x2=input()
        x3=input()
        x1,x2,x3=compare(x1,x2,x3)

        d=[]
        for _ in range(26):
            d.append([])

        for i in range(len(x1)):
            c=ord(x1[i])-ord('a')
            d[c].append(i)

        rightSize=len(x2)- Rightanti(x1,x2) #right x1+x2[Rightanti(x1,x2):]
        leftSize=Leftanti(x1,x2) # left x2[:leftsize]+x1
        x=""
        if leftSize<rightSize:
            x=x2[:leftSize]+x1
        else:
            x=x1+x2[Rightanti(x1,x2):]
        d.clear()
        for _ in range(26):
            d.append([])
        x1=x
        x2=x3
        for i in range(len(x1)):
            c=ord(x1[i])-ord('a')
            d[c].append(i)

        rightSize=len(x2)- Rightanti(x1,x2) #right x1+x2[Rightanti(x1,x2):]
        leftSize=Leftanti(x1,x2) # left x2[:leftsize]+x1
        x=""
        if leftSize<rightSize:
            x=x2[:leftSize]+x1
        else:
            x=x1+x2[Rightanti(x1,x2):]
        print(len(x))

    # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
