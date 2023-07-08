from collections import  defaultdict
def getCombinationSum(candidates,target):
    candidates.sort()
    mp = defaultdict(list)
    for num in candidates:
        for val in range(1,target+1):
            diff = val - num
            if diff==0:
                mp[val].append([num])
            elif diff in mp:
                for ar in mp[diff]:
                    cp = ar.copy()
                    cp.append(num)
                    mp[val].append(cp)
    if target in mp:
        return mp[target]
    else:
        return []
if __name__ == '__main__':
    while True:
        candidates = list(map(int,input().split()))
        target = int(input())
        print(getCombinationSum(candidates,target))
