def isPalindrome(x):
    j=len(x)-1
    for i in range(0,len(x)//2):
        if x[i]==x[j]:
            j-=1
        else:
            return False
    return True
def isMirror(x):
    ans=""
    for i in range(len(x)):
        if x[i] in reverse:
            ans=reverse[x[i]]+ans
    if ans==x:
        return True
    return False

reverse={
    'A':'A', 'H':'H','I':'I','M':'M','O':'O','T':'T','U':'U',
    'V':'V', 'W':'W','X':'X','Y':'Y','1':'1','8':'8',
    'E':'3','J':'L', 'L':'J', 'S':'2','Z':'5','2':'S',
    '3':'E','5':'Z'
}

while True:
    try:
        x=input()
        if not x:
            break
            # print(isPalindrome(x))
        if isMirror(x) and isPalindrome(x):
            print('{} -- is a mirrored palindrome.'.format(x))
        elif isMirror(x):
            print('{} -- is a mirrored string.'.format(x))
        elif isPalindrome(x):
            print('{} -- is a regular palindrome.'.format(x))
        else:
            print('{} -- is not a palindrome.'.format(x))
        print()
    except Exception:
        break