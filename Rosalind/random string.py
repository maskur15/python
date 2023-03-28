#https://rosalind.info/problems/prob/
import math

def RandomString(strRandomString, stringArray):
    strRandomString = strRandomString.upper()
    cg = len(strRandomString.replace('A', '').replace('T', ''))
    at = len(strRandomString.replace('C', '').replace('G', ''))
    inputArray = stringArray.split()
    outputArray = []
    for i in range(0, len(inputArray)):
        prob = cg * math.log10(float(inputArray[i]) / 2) + at * math.log10((1 - float(inputArray[i])) / 2)
        outputArray.append(round(prob, 3))
    return outputArray




result = ' '.join(map(str, RandomString('CGTACCACTTAACGCCGCAAGCCCGTGAAGCCTACGCGTCCACAGTAGCATCTTTATGGAGCAAATATTCCTGAAAAGATACGTGCTTCTGCTTC', '0.091 0.108 0.160 0.251 0.298 0.316 0.404 0.469 0.494 0.563 0.586 0.665 0.693 0.755 0.812 0.867 0.944')))

f = open('PROB.txt', 'w')
f.write(result)
f.close()
