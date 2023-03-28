#https://leetcode.com/problems/subarray-sum-equals-k/
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        map={}
        map[0]=1
        ans=0
        val=0
        for num in nums:
            val+=num
            if val-k in map:
               ans+=map[val-k]
            if val in map:
                map[val]+=1
            else:
                map[val] = 1

        return  ans



 



s =Solution()
print(s.subarraySum([1,3,3,2],0))