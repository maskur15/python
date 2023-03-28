def reverseInteger(x):
    num=0
    f=1
    if x <0:
        x=x*-1
        f=-1
    while x!=0:
        rem=x%10
        if f==1 and num> 2147483648//10:
            return 0
        elif f==1 and num==2147483648//10 and rem>7:
            return 0
        elif f==-1 and num>2147483648//10:
            return 0
        elif f==-1 and num==2147483648//10 and rem>8:
            return 0
        num=num*10+rem
        x=x//10
    return num*f
def reversEInteger(x):
    s=str(x).strip('-')
    s=s[::-1]
    if x>0 and int(s)>=pow(2,31) or x<0 and int(s)>pow(2,31):
        return 0
    if x<0:
        return int(s)*-1
    return int(s)


print(reversEInteger(8939393333321))
