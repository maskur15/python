def solve(nums1,nums2):
    ans=[]
    for n in nums1:
        flag=0
        for v in nums2:
            if flag==-1 and v>n:
                flag=v
                break
            elif flag==0 and n==v:
                flag=-1
        ans.append(flag)
    return ans
if __name__ == '__main__':
    ar1=list(map(int,input().split()))
    ar2=list(map(int,input().split()))
    print(solve(ar1,ar2))