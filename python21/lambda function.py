sum = lambda x,y: x+y
print(sum(3,4))
max=34
def print_max():
    global max
    max=max+3
    print(max)
print_max()