def modify(a):
    return a.split()[1]
name=['sci pox','fix chai','Tom bad','Jom cruel','Dapi aut','dip good']
name.sort()
print(name)

#if we want to sort by second word
#pass the method into key
name.sort(key=modify)
print(name)

#using lambda expression  instead of passing method
num=[44,29,22,18,11,34,23]
#key=lamda followed by variable : function
#sort by second digit
num.sort(key=lambda x : x%10)
print(num)