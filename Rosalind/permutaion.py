#https://rosalind.info/problems/pper/

from math import factorial

def numPartialPerms(n,k):
    perm = (factorial(n)/factorial(n-k)) % 1000000
    return perm

print(int(numPartialPerms(92,8)))