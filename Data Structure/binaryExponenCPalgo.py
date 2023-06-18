def binpow(a,n):
    if n==0:
        return 1
    result = binpow(a,n//2)
    if n%2==0:
        return  result*result
    else:
        return  a* result*result
if __name__ == '__main__':
    print(binpow(2,6))