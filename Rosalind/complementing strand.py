#https://rosalind.info/problems/revc/
def reverse (str):
    reverse = []
    for i in range(len(str)-1, -1, -1):
        reverse.append(str[i])
    for i in range(0, len(reverse)):
        if (reverse[i] == "A"):
            reverse[i] = "T"
        elif (reverse[i] == "T"):
            reverse[i] = "A"
        elif (reverse[i] == "C"):
            reverse[i] = "G"
        else:
            reverse[i] = "C"
    return reverse

print(reverse("AAAACCCGGAT"))