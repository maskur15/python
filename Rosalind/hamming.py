#https://rosalind.info/problems/hamm/
str1 = "GAGCCTACTAACGGGAT"
str2 = "CATCGTAATGACGGCCT"
def Distance(str1, str2):
    count = 0
    for i in range(0, len(str1)):
        if (str1[i] != str2[i]):
            count = count + 1
    return count

print(Distance(str1, str2))