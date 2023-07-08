def solve(nums,target):
    s=0
    pre_index =0
    ans = 9999999999
    for i in range(len((nums))):
        s+=nums[i]
        while s>=target:
            s=s-nums[pre_index]
            ans = min(ans,i-pre_index+1)
            pre_index+=1

    if ans == 9999999999:
        return 0
    return  ans
if __name__ == '__main__':
    while True:
        nums = list(map(int,input().split()))
        target = int(input())
        solve(nums,target)