#function in python
def myfunc():
    print("python function create")
myfunc()
def withArgument(aug):
    print(aug+" !!")
withArgument("word")
def add(x,y):
    print("sum : ",x+y)
add(2,3)




def max(x,y):
    if(x>y):
        return x
    elif(x<y):
        return y
    else:
        return "equal"
print(max(8,3))
print(max(8,8))
#function as object
sum=add
sum(9,8)
del sum