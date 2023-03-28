#https://cp-algorithms.com/algebra/binary-exp.html#algorithm
mod = 1000000007

def powerUsingBinaryExpon(a,n):
    result=1
    while n>0:
        if n&1:
            result=result*a%mod
        a=a*a%mod
        n=n>>1
    return result
def countGood(n):
    return  powerUsingBinaryExpon(5,(n+1)//2)*powerUsingBinaryExpon(4,n//2)%mod
#another approaches using python built in

def countGoodDigit(n):
    mod=10**9+7
    n1= n+1//2
    n2=n//2
    return pow(5,n1,mod) * pow(4,n2,mod) %mod
print(countGoodDigit(50))
