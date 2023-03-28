rfp=0
while True:

    rfp+=1
    n,p=input().split()
    n=int(n)
    p=int(p)

    if not n and not p:
        break
    if rfp>1:
        print()
    for i in range(n):
        input()
    lowerP=0
    bestP=0
    for i in range(p):
        new=input()
        price,number=input().split()
        price=float(price)
        number=int(number)
        for j in range(number):
            input()
        if number>bestP:
            bestP=number
            lowerP=price
            name=new
        elif number == bestP and price<lowerP:
            bestP=number
            lowerP=price
            name=new
    print("REP #{:d}".format(rfp))
    print(name)
