#s=vt 
import  sys
while True:
    input_= sys.stdin.readline()
    if input_=='':
        break
    v,t=input_.split()
    print(int(v)*2*int(t))