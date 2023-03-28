x,y,z=map(int,input().split())
if x==y and z==0:
    print(0)
elif x==y and z!=0:
    print('?')
elif x>y and z==0:
    print('+')
elif x>y and z!=0:
    if y+z>=x:
        print('?')
    else:
        print('+')

elif x<y and z==0:
    print('-')
elif x<y and z!=0:
    if x+z>=y:
        print('?')
    else:
        print('-')
