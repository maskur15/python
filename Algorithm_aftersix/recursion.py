n= int(input())
def recursion(n):
    if n==1:
        return 1
    print(n)
    return  n*recursion(n-1)
print("recursion: ",recursion(n))

def BinaryExpon(a,n):
    if n==0:
        return 1
    res = BinaryExpon(a,n//2)
    if n%2==0:
        return res*res*a
    else:
        return res*res
print(BinaryExpon(6,3))