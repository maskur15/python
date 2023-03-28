i=0
while True:
    i+=1
    x=input()
    if x=='*': break
    print('Case {}: '.format(i),end='')
    if x=='Hajj':
        print('Hajj-e-Akbar')
    else:
        print('Hajj-e-Asghar')