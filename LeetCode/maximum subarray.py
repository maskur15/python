def maxsum(arr):
    s=m= arr[0]

    for i in range(1,len(arr)):
        s= max(arr[i],s+arr[i])
        if s>m:
            m=s
    return m
arr=list(map(int,input().split()))
print(maxsum(arr))