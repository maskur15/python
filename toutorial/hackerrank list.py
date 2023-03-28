if __name__ == '__main__':
    n = int(input())
    var =list()
    for i in range(n):
        x=list(input().split())
        if x[0]=="insert":
            var.insert(int(x[1]),int(x[2]))
        elif x[0]=="print":
            print(var)
        elif x[0]=="remove":
            var.remove(int(x[1]))
        elif x[0]=="append":
            var.append(int(x[1]))
        elif x[0]=="sort":
            var.sort()
        elif x[0]=="pop":
            var.pop()
        elif x[0]=="reverse":
            var.reverse()







