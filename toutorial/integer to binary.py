def binary(num):
    x=""
    while num:
        x= str(num&1)+x
        num=num>>1
    print(x)
binary(10)