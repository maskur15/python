ant=[i for i in range(10)]
for i in range(len(ant)):
    for j in range(i+1,len(ant)):
        for k in range(j+1,len(ant)):
            print(i,j,k,end='/ ')
        print()
    print()
