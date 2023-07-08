def solve(nums):
    pre =0
    ans =0
    zero =0
    one =0
    pre =0
    for v in nums:
        if v==0 :
            zero+=1
            ans = max(ans,pre+one)
            if zero==1:
                 pre = one
            else:
                pre =0
            one =0
        else:
            one+=1
            zero=0
    ans =max(ans,pre+one)
    if ans ==len(nums):
        ans -=1
    return  ans
if __name__ == '__main__':

    while True:
        nums = list(map(int,input().split()))
        print(solve(nums))