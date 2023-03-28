import  sys
while True:
    inp = sys.stdin.readline()
    if inp=='': break
    a,b,c= map(int,inp.split())
    if a==b and b==c:
        print('*')
    elif a==b : print('C')
    elif a==c: print('B')
    elif b==c: print('A')