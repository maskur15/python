parents = [i for i in range(26)]
def find(x):
    if (x != parents[x]):
        parents[x] = find(parents[x])
    return parents[x]
def union(x, y):
    r1 = find(x)
    r2 = find(y)
    if (r1 != r2):
        parents[r1] = r2
import sys
input = sys.stdin.readline
seen = [False] * 26
d = {}
for _ in range(int(input())):
    s = input().rstrip()
    for j in s:
        seen[ord(j) - 97] = True
        union(ord(s[0]) - 97, ord(j) - 97)
ans = 0
for i in range(0, 26):
    if (seen[i] and parents[i] == i):
        ans += 1
print(ans)