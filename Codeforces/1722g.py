##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
def xor(ar):
    c=0
    for a in ar:
        c=c^a
    return  c
def show(x1,x2):
    if len(x1)==len(x2):
        for i in range(len(x1)):
            print(x2[i],x1[i],end=' ' ,sep=' ')
            if i==len(x1)-1:
                print()
    elif len(x1)>len(x2):
        for i in range(len(x2)):
            print(x1[i],x2[i],end=' ',sep=' ')
        print(x1[len(x1)-1])
    else:
        for i in range(len(x1)):
            print(x2[i],x1[i],end=' ' ,sep=' ')
        print(x2[len(x2)-1])


def anti(n):
   x1=list()
   x2=list()
   m1=n//2+n%2
   m2=n//2

   if m1%2==0 and m2%2==0:
       c1=0
       c2=4
       f=True
       for _ in range(m2):
           if f:
               x1.append(c1)
               x1.append(c1 + 1)
               f = False
               c1 += 4
           else:
               x2.append(c1)
               x2.append(c1 + 1)
               f = True
               c1+=4
   elif m1%2!=0 and m2%2!=0:
       c1 = 0
       c2 = 4
       f = True
       for _ in range(m2-1):
           if f:
               x1.append(c1)
               x1.append(c1 + 1)
               f = False
               c1 += 4
           else:
               x2.append(c1)
               x2.append(c1 + 1)
               f = True
               c1 += 4
       shift1=(n*2)^1
       x1.pop(1)
       x1.append(n*2)
       x1.append(shift1)
       shift2=(n*2+8)^4
       x2.pop(0)
       x2.append((n*2+8))
       x2.append(shift2)
   else:
       if m1%2!=0:
           t=m2
           m2=m1
           m1=t
       if m1>m2:
           c1 = 0
           c2 = 4
           f = True
           for _ in range(m1):
               if f:
                   x1.append(c1)
                   x1.append(c1 + 1)
                   f = False
                   c1 += 4
               else:
                   x2.append(c1)
                   x2.append(c1 + 1)
                   f = True
                   c1 += 4
           x1.pop(0)
       else:
           c1 = 4
           f = True
           for _ in range(m1):
               if f:
                   x1.append(c1)
                   x1.append(c1 + 1)
                   f = False
                   c1 += 4
               else:
                   x2.append(c1)
                   x2.append(c1 + 1)
                   f = True
                   c1 += 4
           x1.append(0)



  # print(x1,xor(x1))
  # print(x2,xor(x2))
   show(x1,x2)



if __name__ == '__main__':
    test=int(input())
    while test:
        test-=1
        n=int(input())
        anti(n)
 # That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.

