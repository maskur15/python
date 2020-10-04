#string operation
my_string = 'HEllo world BANGLADESH'
print(my_string[4])
#accessing subset of a string
print(my_string[1:4]);
print(my_string[:4]) ;
print("hello"*10)
#splitting string
print('Source string :',my_string)
print(my_string.split(" "))
#COUNTING STRINGS
print(my_string.count(" "))
#replacing string
print(my_string.replace("BANGLADESH","aMERICA"))
#find the substring
print(my_string.find('world'))
#converting other types into string
message = " hwllo we love you" +str(211)
print(message)