# https://codeforces.com/contest/1263/problem/D
import sys

input = sys.stdin.readline
if __name__ == '__main__':
    test = int(input())
    ds = {}
    while test:
        test -= 1
        x = input().rstrip()
        pr = x[0]
        if x[0] in ds:
            pr = ds[x[0]]
        for ch in x:
            pch=ch
            if ch in ds:
                pch=ds[ch]
                ds[pr]=pch
            else:
                ds[ch] = pr
    ans=0
    for a in ds:
        if a==ds[a]:
            ans+=1
    print(ans)
