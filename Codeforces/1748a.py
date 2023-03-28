##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
if __name__ == '__main__':

    t=int(input())
    while t:
        t-=1
        n=int(input())
        ar=[{0:0,1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0} for _ in range(n)]
        s=input()
        ar[0][int(s[0])]+=1
        for i in range(1,len(s)):
            ar[i]=ar[i-1].copy()
            ar[i][int(s[i])]+=1
        for i in range(n):
            k=i
            for j in range(i,n):
                
        print(ar)



# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
