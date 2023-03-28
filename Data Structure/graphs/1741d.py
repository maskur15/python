##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK

from math import log2
if __name__ == '__main__':
    t=int(input())
    while t:
        t-=1
        tree = list()
        n=int(input())
        arr=list(map(int,input().split()))
        for i in range(n):
            tree.append(-1)
        tree=tree+arr
        pw=int(log2(n))-1
        ln=n
        count=0
        d=1
        while pw>=0:
            i=int(pow(2,pw))
            temp=i
            while i<ln:
                left = tree[i*2]
                right=tree[i*2+1]
                if abs(left-right)==d:
                    if left>right:
                        count+=1
                        tree[i]=left
                    else:
                        tree[i]=right
                else:
                    count=-1
                    break
                i+=1
            pw-=1
            d=d*2
            ln=temp
            if count==-1:
                break
        print(count)

# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
