#https://rosalind.info/problems/sign/
import itertools

n = 6
permutation = []
total = 0
c = itertools.permutations(list(range(1, n + 1)))

for i in c:
    d = itertools.product([-1, 1], repeat = len(list(range(1, n + 1))))
    for j in d:
        e = [i * sign for i, sign in zip(i, j)]
        permutation.append(e)
        total = total + 1

print(total)

for i in range(0, len(permutation)):
    print(*permutation[i], sep=' ')