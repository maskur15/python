# Loop in python
print("While loop in python")
i=1
while i<=5:
    print(i)
    i=i+1
print("end of while loop")
while i<=10:
    print(i)
    i=i+1
    if i==8 :
        print("Brek statement execute")
        break
i=0
while True:
    i+=1
    if i==2:
        print("Skipping 2")
        continue
    if i==5:
        print("Breaking")
        break
    print(i)
print("Finished!!")
#for looop in python
print("for loop in python")
words=['hello','my','Brother']
for word in words:
    print(word+'!!')
for number in range(5,9,2): #range use to create set of number
    print(number)
