def is_prime(n,i=2):
    if n==1:
        return False
    if i*i>n:
        return True
    if n%i==0:
        return False
    else:
         return is_prime(n,i=i+1)
def swap(a,b):
    return b,a

print(is_prime(int(input())))
a,b=map(int,input().split())
print(swap(a,b))