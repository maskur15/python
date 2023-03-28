from sys import  stdin

if __name__ == '__main__':
    try:
        for inp in stdin:
                n,s= inp.split()
                d = {}
                size = int(n)
                password = s[:size]
                for i in range(len(s) - size + 1):
                    d[s[i:i + size]] = 1 + d.get(s[i:i + size], 0)
                    if d[s[i:i + size]] > d.get(password, 0):
                        password = s[i:i + size]
                print(password)
    except EOFError:
        pass

