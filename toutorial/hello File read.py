#file system in python
myfile = open("D:\File/test.text","r")
print(myfile.read(45))
#readlines return an list of all line in the text file
cont = myfile.readlines();
for i in cont:
    print(i)
myfile.close()