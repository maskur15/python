def  leetPow(x,n):
    if n==0:
        return 1
    res = leetPow(x,n//2)
    if n%2==0 :
        return res*res
    return x*res*res
if __name__ == '__main__':
    while True:
        x,n = map(float,input().split())

        result = (leetPow(x,abs(int((n)))))
        if n<0:
            print(1/result)
        else:print(result)
