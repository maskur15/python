#robot instruction 12503 is the  id
try:
    test = int(input())
    while test:
        test-=1
        n=int(input())
        index=list()
        pos=0
        while n:
            n-=1
            ins=input().split()
            if ins[0]=='LEFT':
                index.append(-1)
                pos+=-1
            elif ins[0]=='RIGHT':
                index.append(1)
                pos+=1
            else:
                index.append(index[int(ins[2])-1])
                pos+= index[int(ins[2])-1]
        print(pos)

except Exception:
    quit()