def reverse(x):
    num=0
    while x:
        num=num*10+x%10
        x=x//10
    return num
def palindrome(x):
    if x==reverse(x):
        return  True
test=int(input())
while test:
    test-=1
    x=int(input())
    count=0
    while True:
        if palindrome(x):
            print(count,x)
            break
        else:
            x=x+reverse(x)
            count+=1
