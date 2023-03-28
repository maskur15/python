#https://rosalind.info/problems/revp/
f=open("temp.txt",'r')
string=f.read()
strDNA = ''.join(string.splitlines());
def ReverseComplement(strDNA):
    result = ""
    for i in range(len(strDNA) - 1, -1, -1):
        if (strDNA[i] == "A"):
            result += "T"
        elif (strDNA[i] == "T"):
            result += "A"
        elif (strDNA[i] == "C"):
            result += "G"
        else:
            result += "C"
    return result


def IsReverseComplement(strDNA):
    return (strDNA == ReverseComplement(strDNA))


def RestrictionSites(strDNA):
    resultList = []
    for i in range(4, 13):
        for j in range(0, len(strDNA) - i + 1):
            if (IsReverseComplement(strDNA[j:j + i])):
                resultList.append(str(j + 1) + ' ' + str(i))
    return resultList


for dna in RestrictionSites(strDNA):
    print(dna)