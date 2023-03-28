dict={}
for i in range(26):
    dict[i]=chr(97+i)
    dict[chr(97+i)]=i
def cipherEncrypt(text):
    x=""
    for ch in text:
        x+=dict[(dict[ch]+3)%26]
    return x
def cipherDecrypt(text):
    x=""
    for ch in text:
        x+=dict[(dict[ch]-3)%26]
    return  x
print('Enter plain text: ')
txt=input()
dc=cipherEncrypt(txt)
print(cipherEncrypt(txt))
print(cipherDecrypt(dc))
print(-3/26)
