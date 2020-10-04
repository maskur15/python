#list in python
words =['hello','world','start','from']
print(words[0])
print(words[1],words[2])
emptyList =[]
print(emptyList)
number = list(range(8))
print(number)
#list function
print("//list function")
number.append(words)
print(number)
print("lenth of the list : ",len(number))
index=2
number.insert(index,"maskur")
print(number)
print(number.index(2))
if "maskur" in number:
    print("Maskur is in the list")
elif "hasan" in number:
    print("hasan is  in the list")
else:
    print("End")
#list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
#list comprehension can be use with if condition
cubes= [i*2 for i in range(10) if  i%2==0]
print(cubes)
