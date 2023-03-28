if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    num=list(arr)
    max=max(num)
    num.sort();

    while(n>=0):
        n-=1
        if(num[n]<max):
          print(num[n])
          break


