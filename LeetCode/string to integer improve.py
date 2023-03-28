def stringToint(s):
    s=s.strip()
    sign=1
    num=0
    if len(s)==0:
        return 0
    if s[0]=='-':
        sign=-1
    elif s[0]=='+':
        sign=1
    elif s[0].isnumeric():
        num= ord(s[0])- ord('0')
    else:
        return  0

    for i in range(1,len(s)):
        if s[i].isnumeric():
            num=num*10+(ord(s[i])-ord('0'))
            if num * sign > 2147483647:
                return 2147483647
            elif num * sign < -2147483648:
                return -2147483648
        else:
            break
    return num*sign

print(stringToint('42 444 '))