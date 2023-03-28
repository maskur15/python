x=input();
if(x[0]=='-'):
    t1=x[len(x)-1]
    t2=x[len(x)-2]
    if(int(t1)>int(t2)):
        x.__reduce__()
else:
    print(x)