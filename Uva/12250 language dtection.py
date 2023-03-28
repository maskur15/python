import  sys
d={'HELLO':'ENGLISH','HOLA':'SPANISH','HALLO':'GERMAN'
   ,'BONJOUR':'FRENCH','CIAO':'ITALIAN','ZDRAVSTVUJTE':'RUSSIAN'}
i=1
while True:

    inp = input()
    if inp=='#':
        break
    print('Case {}: '.format(i),end='')
    if inp in d:
        print(d[inp])
    else:print('UNKNOWN')
    i+=1