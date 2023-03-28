#https://rosalind.info/problems/gc/
string = ["CCTGCGGAAGATCGGCACTAGAATAGCCAGAACCGTTTCTCTGAGGCTTCCGGCCTTCCCTCCCACTAATAATTCTGAGG", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT", "CCACCCTCGTGGTATGGCTAGGCATTCAGGAACCGGAGAACGCTTCAGACCAGCCCGGACTGGGAACCTGCGGGCAGTAGGTGGAAT"]
m = []
def Content(n):
    for i in n:
        count = 0
        for j in range(0, len(i)):
            if (i[j] == 'C' or i[j] == 'G'):
                count = count + 1
        l = count/len(i)
        m.append(l)
    large = 0
    for k in m:
        if (k > large):
            large = k
    return large*100

print(Content(string))