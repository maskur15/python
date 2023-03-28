#https://rosalind.info/problems/tree/

f = open('temp.txt', 'r')
str1 = ' '
mat = []
while (str1 != ''):
    str1 = f.readline().strip()
    mat.append(str1)
mat.remove('')

n = int(mat[0])
#Takes the number of nodes n minus the total number of edges the adjaceny list minus one
#len(mat) = number of edges in the adjaceny list - 1
edge = n - len(mat)

print(edge)