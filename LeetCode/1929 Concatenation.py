def concate(nums):
    a=len(nums)
    for i in range(a):
        nums.append(nums[i])
    return nums

n=[1,2,3]
print(concate(n))