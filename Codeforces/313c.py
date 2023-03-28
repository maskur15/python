from math import log2
def main():
    n = int(input())
    ar =list(map(int,input().split()))
    ar.sort(reverse=True)
    p = log2(n)//2

    inc=0
    i=0
    r=1
    ans=sum(ar)
    while True:
       # print(ar[i:r],sum(ar[i:r]),p,r)
        ans+=sum(ar[i:r])*p
        p-=1
        if r>=(n//4):
            break

        i=r
        r=i+i*3

    print(int(ans))

if __name__=='__main__':
         main()