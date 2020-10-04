def computeXor(n):
    if n%4==0:
        return n
    if n%4==1:
        return 1
    if n%4==2:
        return n+1
    if n%4==3:
        return 0
if __name__=="__main__":
    n = int(input())
    print(computeXor(n))