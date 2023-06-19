def sumuptoNth(n):
    if n==0:
        return n
    return sumuptoNth(n-1) + n
if __name__ == '__main__':
    print(sumuptoNth(5))