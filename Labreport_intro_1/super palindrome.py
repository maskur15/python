def superpalindrome(left,right):
    def reverseeven(x):
        str = ""
        for i in range(len(x)):
            str = x[i] + str
        return x + str

    def reverseodd(x):
        str = ""
        for i in range(len(x) - 1):
            str = x[i] + str
        return x + str

    def ispalindrome(x):
        str = ""
        for i in range(len(x)):
            str = x[i] + str
        if x == str:
            return True
        else:
            return False

    size = 100000
    ans = 0

    for i in range(1, size):
        x1 = str(i)
        x2 = reverseeven(x1)
        num = int(x2) * int(x2)
        if (num >= left and num <= right):
            # print(x2, " ", num)
            x = str(num)
            if ispalindrome(x):
                ans += 1
        i += 1
    for i in range(1, size):
        x1 = str(i)
        x2 = reverseodd(x1)
        num = int(x2) * int(x2)
        if (num >= left and num <= right):
            # print(x2, " ", num)
            x = str(num)
            if ispalindrome(x):
                ans += 1
        i += 1
    return  ans

if __name__=='__main__':
    left,right= map(int,input().split())
    print(left," ",right)
    superpalindrome(left,right)
