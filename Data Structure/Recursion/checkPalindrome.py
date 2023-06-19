def isPalindrome(x):
    if len(x)==1:
        return  True
    elif x[0] != x[len(x)-1]:
        return False
    else:
        return isPalindrome(x[1:len(x)-1])
if __name__ == '__main__':
    x= 'racecar1'
    print(isPalindrome(x))
