#https://rosalind.info/problems/perm/
import itertools
n = 5
perm = list(itertools.permutations(range(1, n + 1)))

f = open('temp.txt', 'w')
f.write(str(len(perm)))
f.write("\n")
for i in perm:
    f.write(' '.join(str(j) for j in i))
    f.write("\n")
f.close()