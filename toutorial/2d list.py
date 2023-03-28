class Solution:
    def convert(self,s: str, numRows: int) -> str:
        arr = []*numRows
        print(arr)

#dont use this way for 2d array it will use the same object
arr=[[0]*5]*5
arr[0].append(4)
arr[0].append(5)
arr[4].append(3)
print(arr)
#use this way
def twodaray():
    n,m=map(int,input().split())
    ar=list()
    for _ in range(n):
        br=list(map(int,input().split()))
        ar.append(br)

def twdarray():
    ar=[[0]*5 for _ in range(5)]
    print(ar)
twdarray()

def twodEmptyarray():
    n = int(input('Enter number of node : '))
    g = [[] * n for _ in range(n)]
    for i in range(n):
        x, y = map(int, input().split())
        g[x].append(y)

    for i in range(n):
        print(i, ": ", g[i])
if __name__ == '__main__':
    twodEmptyarray()
