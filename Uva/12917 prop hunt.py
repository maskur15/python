import sys
while True:
    inp = sys.stdin.readline()
    if inp=='': break
    p,h,o=map(int,inp.split())
    d=o-p
    if h>d: print('Hunters win!')
    else: print('Props win!')