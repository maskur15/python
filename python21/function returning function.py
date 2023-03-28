def make_checker(s):
    if s== 'even':
        return lambda n: n%2==0
    elif s=='positive':
        return  lambda  n: n>=0
    elif s=='negative':
        return lambda  n: n<0
    else:
        raise ValueError('unknown request')
f1=make_checker('even')
print(f1(3))
def make_function():
    def add(x,y):
        return x+y
    return add
f2=make_function()
print(f2(3,9))