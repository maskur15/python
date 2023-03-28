import sys
while True:
    inp = sys.stdin.readline()
    if inp=='': break
    x,y=map(int,inp.split())
    print(abs(x-y))