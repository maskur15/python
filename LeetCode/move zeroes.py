if __name__ == '__main__':
    nums=list(map(int,input().split()))
    i=0
    j=0
    while i< len(nums) and j<len(nums):
        if nums[i]==0:
            if nums[j]!=0:
                nums[i]=nums[j]
                j+=1
                i+=1
            else:
                j+=1
        else:
            j+=1
            i+=1





    print(nums)
