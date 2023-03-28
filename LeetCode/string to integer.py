def stringtointeger(s):
    num=0
    sign=1
    fsing=1
    flag=False
    fchar=True
    for i in s:
        if i==' ' and  fchar:
            continue
        elif i=='-' and fsing==1 and fchar:
            fchar=False
            fsing=2
            sign=-1
        elif i=='+' and fsing==1 and fchar:
            fchar=False
            sign=1
            fsing=2

        elif i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9' or i=='0':
            num=num*10+ int(i)
            fchar=False
            flag=True
            if num * sign > 2147483647:
                return 2147483647
            elif num * sign < -2147483648:
                return -2147483648
        else:
            break



    num=num*sign

    return num
print(stringtointeger("    999-- j0000042a1234"))
print(ord('3'))




