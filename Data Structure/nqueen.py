def isValid(ar,in1,in2):
    i=in1; j=in2
    while j+1<len(ar):
        if ar[i][j+1]==1 : return False
        j+=1
    i=in1;j=in2

    while j-1>=0:
        if ar[i][j-1]==1: return False
        j-=1
    i=in1;j=in2

    while i+1<len(ar):
        if ar[i+1][j]==1: return False
        i+=1
    i=in1;j=in2

    while i-1>=0:
        if ar[i-1][j]==1:
            return False
        i-=1
    i=in1;j=in2


    #diagonal
    while i+1<len(ar) and j+1<len(ar):
        if ar[i+1][j+1]==1: return False
        i+=1
        j+=1
    i=in1;j=in2

    while i-1>=0 and j-1>=0:
        if ar[i-1][j-1]==1: return False
        i-=1
        j-=1
    i=in1;j=in2

    while i-1>=0 and j+1<len(ar):
        if ar[i-1][j+1]==1: return  False
        i-=1
        j+=1
    i=in1;j=in2

    while i+1<len(ar) and j-1>=0:
        if ar[i+1][j-1]==1: return False
        i+=1
        j-=1

    return True
def nqueen():
    n=4
    queen=[0]*4
    ar=list()
    for i in range(4):
        a=[0]*4
        ar.append(a)
    i=j=0
    print(ar)
    while j<n:
            while i<n:
                if isValid(ar,i,j):
                    ar[i][j]=1
                    queen[j]=i
                    i=0
                    j+=1
                    break
                i+=1
            if i==n:
                ar[queen[j-1]][j-1]=0
                j-=1; i=queen[j-1]+1

    print(ar)



nqueen()