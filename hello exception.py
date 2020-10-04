#exception in python
try:
    num1= 2
    num2= 0
    print(num1/num2)
    print("calculationn done")
except ZeroDivisionError:
    print("an error occoured")
print("\nnew block start")
try:
    variable = 10
    print(variable+"hello")
    print(variable/2)
except (ZeroDivisionError,TypeError):
    print("error occoured")
try:
    variable = 23
    print(variable/0)
except:
    print("new error")

finally:
    print("always print")
print(2)
assert  2+2 == 43
print(3)