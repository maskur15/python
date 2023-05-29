#sliding window
class Solution:
    def subArraySum(self,arr,n,s):
        index =0
        sum=0
        preindex =0
        while index<n:

            if sum+arr[index] == s:
                return [preindex+1,index+1]
            elif sum+arr[index]<s:
                sum+=arr[index]
                index+=1
            elif sum>=arr[preindex]:
                sum-=arr[preindex]
                preindex+=1
            else:
                index+=1
                preindex = index
                sum=0

        return [-1]

if __name__ == '__main__':
    s = Solution()
    ans = s.subArraySum([1,2,3,7,5],5,12)

    for i in ans:
        print(i,end=' ')