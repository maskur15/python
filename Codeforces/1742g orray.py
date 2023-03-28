##I try various [strategies], and one of them is the right one.
# I am no genius. I am simply good at it.
# BY-GK
def mergeSort(arr):
    if len(arr) == 1:
        return arr
    ind = len(arr) // 2
    left = arr[:ind]
    right = arr[ind:]
    mergeSort(left)
    mergeSort(right)
    i = k = j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            arr[k] = left[i]
            i += 1
            k += 1
        else:
            arr[k] = right[j]
            j += 1
            k += 1
    while i < len(left):
        arr[k] = left[i]
        k += 1
        i += 1
    while j < len(right):
        arr[k] = right[j]
        k += 1
        j += 1
    return arr


def Or(ar):
    for i in range(1, len(ar)):
        ar[i] = ar[i] | ar[i - 1]
    return ar


if __name__ == '__main__':

    test = int(input())
    while test:
        test-=1
        n=int(input())
        ar=list(map(int,input().split()))
        if len(ar)==1: print(ar[0],end=' ')
        elif len(ar)==2: print(max(ar),min(ar),end=' ')
        else:
            if ar[1]>ar[0]:print(ar[1],ar[0],*ar[2:],sep=' ',end=' ')
            elif ar[2]>ar[0]:
                print(ar[2],ar[0],ar[1],end=' ')
                if len(ar)>3: print(*ar[3:],sep=' ',end=' ')

            else:
                if ar[0]|ar[1]<ar[0]|ar[2]:
                    print(ar[0],ar[2],ar[1],end=' ')
                    if len(ar) > 3: print(*ar[3:], sep=' ',end=' ')

                else:
                    cm=Or(ar.copy())
                    print(ar[0],end=' ')
                    for i in range(1,len(cm)):
                        if cm[i]==cm[i-1]:
                            if i+1<len(cm) and cm[i+1]>cm[i]:
                                print(ar[i+1],ar[i],end=' ')
                                if i+2<len(cm): print(*ar[i+2:],sep=' ',end=' ')
                                break
                            else:
                                print(ar[i],end=' ')
                        else:
                            if i==1: print(ar[i],end=' ')
                            else:
                                print(ar[i],ar[i-1],end=' ')
                                if i+1<len(ar):print(*ar[i+1:],sep=' ',end=' ')
        print()







# That is the favor of Allah, which He gives to whom He wills, and Allah is the possessor of Ultimate favor.
