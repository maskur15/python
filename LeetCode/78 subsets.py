ans =[]
def add(n,ar):
    if n==1:
        ans.append([1])
        return 1
    ar.append(n)
    ans.append(ar)
    v = add(n-1,[])
    ar.append(v)
    ans.append(ar)


if __name__ == '__main__':
    while True:
        add(3,[])
        print(ans)
        break


