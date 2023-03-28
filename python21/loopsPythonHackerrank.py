import re

#check weather a string is alphanumeric or not
string = bool(re.match('^[a-zA-Z0-9]+$', 'string'))


def do(stirng):
    l = len(string)
    for i in range(l-1):
        j = i + 1

        if re.match('^[a-zA-Z0-9]+$', string[i]):
             if string[i] == string[j]:
                return string[i]


    return -1


string = input()
print(do(string))