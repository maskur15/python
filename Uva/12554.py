song="Happy birthday to you Happy birthday to you Happy birthday to Rujia Happy birthday to you".split()
n=int(input())
name=[]
for _ in range(n):
    a=input()
    name.append(a)
if n<=len(song):
    i=0
    k=0
    while i<len(song):
        print('{}: {}'.format(name[k], song[i]))
        k+=1
        i+=1
        if k==n:
            k=0

else:
    i = 0
    k = 0
    c=n//16
    while i < len(song):
        print('{}: {}'.format(name[k], song[i]))
        k += 1
        i += 1
        if i==len(song) and c>=1:
            c-=1
            i=0
        if c==0:
            break
    if n%16>0:

        while i<len(song):
            print('{}: {}'.format(name[k],song[i]))
            k+=1
            i+=1
            if k==n:
                k=0
