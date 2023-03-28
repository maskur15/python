n=int(input())
a1=input()
a2=input()
a3=input()
a4=input()
a5=input()
x=""
for i in range(0,len(a4),4):
    if a4[i]=='.' and a4[i+1]=='*':
        x+='1'
    elif a4[i]=='*' and a4[i+1]=='.':
        x+='2'
    elif a4[i]=='.' and a4[i+1]=='.':
        x+='3'
print(x)