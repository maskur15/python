##here in this program we will going to learn control flow in python
print(" hello control in python")
print(8>9)
print (8<9)
print(8>=9)
print(8<=8)
boolean = True
print(boolean)
if 10<4:
    print("10 greater than 5")
    print("it ' osk")
print("program end");
#Nested if statement
num1=9
if num1>4:
    print(num1,"is greater than 4")
    if num1<8:
        print(num1,"is less than 8")
        if num1>10:
            print(num1," is greater than 10")
    else:
        print(num1,"is greater than 8")
print("program end!!!");
#if elif or else if
num2=7
if num2 ==3:
    print("The number is 3")
elif num2<3:
    print("The number is less than 3")
else:
    print("the number is greater than 3")
#Boolean logic
if 1!=1 and 2==2:
    print(True)
else:
    print(False)
if 1==1 or 2==3:
    print("True")
#Boolean not opearator
if not 1==1:
    print("Fase")
else :
    print("True")
print("operator precedence!! ")
#operator precedence
if False==False or True:
    print(True)
