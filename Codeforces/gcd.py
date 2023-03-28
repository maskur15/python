def gcd(a,b):
    if b%a==0:
        return  a
    return gcd(b%a,a)
if __name__ == '__main__':
    print(gcd(24,40))