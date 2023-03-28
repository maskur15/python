#https://rosalind.info/problems/subs/
def substring (str, sub):
    list = []
    for i in range (0, len(str) - len(sub)):
        a = str[i:i+len(sub)]
        if (a == sub):
            list.append(i+1)
    return list

print(*(substring("GATATATGCATATACTT", "ATAT")))