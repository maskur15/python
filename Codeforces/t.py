##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
#BY-GK
from collections import defaultdict
def solve(nums,k):
    d= dict()
    ans=[[] for _ in range(len(nums))]
    m=1
    for v in nums:
        if v in d: d[v]+=1
        else:
            d[v]=1
    for v in d:
        ans[d[v]].append(v)
    result=[]
    for i in range(len(ans)-1,-1,-1) :
        result.extend(ans[i])
    return (result[:k])

if __name__ == '__main__':
    print(solve([1,1,1,1,1,2,2,3,3],2))
# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
