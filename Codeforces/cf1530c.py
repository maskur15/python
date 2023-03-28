##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK

def solve():
     n,k=map(int,input().split())
     if n==k: return  1
     if n>k:
         if n%k==0: return  1
         else: return 2
     return k//n if k%n==0 else k//n+1
if __name__ == '__main__':
    tes=int(input())
    while tes:
        tes-=1
        print(solve())
# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
