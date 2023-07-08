def solve_merge(ar1,ar2):
    ins_index = len(ar1)-1
    i = len(ar1)- len(ar2)-1
    j = len(ar2)-1
    while i>=0 and j>=0:
        if ar1[i]>ar2[j]:
            ar1[ins_index] = ar1[i]
            i-=1
            ins_index-=1
        else:
            ar1[ins_index] = ar2[j]
            j-=1
            ins_index-=1

    while j>=0:
        ar1[ins_index] = ar2[j]
        j-=1
        ins_index-=1
    return ar1

if __name__ == '__main__':
    while True:
         ar1 = list(map(int,input().split()))
         ar2 = list(map(int,input().split()))
         ar = solve_merge(ar1,ar2)
         print(ar)




