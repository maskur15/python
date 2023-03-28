#https://cp-algorithms.com/algebra/binary-exp.html#algorithm
def powerUsingBinaryExpon(a,n):
    result=1
    while n>0:
        if n&1:
            result=result*a
        a=a*a
        n=n>>1
    return result

