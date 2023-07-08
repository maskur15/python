from collections import  defaultdict
def getCombinationSum(candidates,target):
    candidates.sort()
    mp = defaultdict(list)

    print(mp)
    mp[1].append([2,4,6])
    mp[1].append([2,15,5])
    mp[3].append([1,2,4])

    for v in mp:
        print(v)
    print(mp)
    for v in mp:
        print(v,': ')
        for ar in mp[v]:
            print(ar)

if __name__ == '__main__':
    while True:
        candidates = list(map(int,input().split()))
        getCombinationSum(candidates,7)
        print(candidates)