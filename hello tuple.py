#tuple in python
#tuple is unlike list where we can not reassign the value as we can in list
words = ("start","game","hiary","aoing","jaipa")
print(words[3])
#words[start:stop:step]
print(words[2:4:1])
emptyTuple = ()
list = [3,3,33,32,55,93,45,9]
dictionary={2:"run",3:"play",4:"success"}
tuple=(3,'e',9,"maskur")
print(dictionary[3])
print(list[::2])
sqs = [0,1,4,9,16,25,36,49,64,81]
print(sqs[1::4])
print(sqs[2:-1])
#list comprehension
cubes = [i**3 for i in range(5)]
print(cubes)
#list comprehension can be use with if condition
cubes= [i*2 for i in range(10) if  i%2==0]
print(cubes)