#https://rosalind.info/problems/fib/
def fibonacci(n,k):
    seq = []
    num = 0
    for i in range (0, n):
        if (i == 0 or i == 1):
            seq.append(1)
        else:
            num = seq[i-1] + seq[i-2]*k
            seq.append(num)
    return seq[len(seq)-1]

print(fibonacci(5,31))