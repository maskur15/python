#http://rosalind.info/problems/revc/
dna=list("GCTA")
dict ={"A":"T","T":"A","C":"G","G":"C"}
for i in range(0,len(dna)):
    dna[i]=dict[dna[i]]
print("".join(reversed(dna)))