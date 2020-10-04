#Codeforces.............
test= int(input())
while test>0:
    num1= int(input())
    i1=1;i2=1
    s1=0;s2=0;
    while i1<num1/2:
        s1+=2**i1
        i1+=1
    s1+=2**num1
    i1=num1/2
    while i1 <num1:
        s2+=2**i1
        i1+=1
    print(int(s1-s2))
    test-=1
