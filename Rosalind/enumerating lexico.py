#https://rosalind.info/problems/lexf/

import itertools

f = open("temp.txt", "r")
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove("")

a = mat[0]
b = int(mat[1])

c = list(map(str, a.split()))
x = list(itertools.product(c, repeat = b))


print(*[''.join(i) for i in x], sep='\n')